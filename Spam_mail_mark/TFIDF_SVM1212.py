#!/usr/bin/python
# -*- coding:latin1-
from pyspark import SparkContext,SparkConf
Conf=SparkConf()
Conf.setAppName("TestApp").set("spark.driver.maxResultSize","4g")
sc = SparkContext(conf = Conf)

import os
from os.path import join
import numpy as np
dest = "/home/15182687/"
ham = []
spam = []
i = 0
for root, dirs, files in os.walk( dest ):
	for OneFileName in files :
		try:
			if OneFileName.find( '.txt' ) == -1 :
            			continue
			OneFullFileName = join( root, OneFileName )
                        fil = []
                        for line in open(OneFullFileName,'r'):
				fil.append(line.strip('\n'))
                        fil =' '.join(fil)
        		if OneFileName.find('ham')  != -1:
            			ham.append(fil)
        		elif OneFileName.find('spam') != -1:
            			spam.append(fil)
		except:
            		pass

print 'data load already'
print len(ham)
from pyspark.mllib.classification import SVMWithSGD
svm = SVMWithSGD()

from pyspark.mllib.feature import HashingTF,IDF
tf = HashingTF(numFeatures = 160000)
idf = IDF()

ham = sc.parallelize(ham).map(lambda email:email.split(' '))
spam = sc.parallelize(spam).map(lambda email:email.split(' '))

hamFeatures = tf.transform(ham)
spamFeatures = tf.transform(spam)

Features = hamFeatures.union(spamFeatures)

idfmodel = idf.fit(Features)
hamFeatures = idfmodel.transform(hamFeatures)
spamFeatures = idfmodel.transform(spamFeatures)

from pyspark.mllib.regression import LabeledPoint
hamTraindata = hamFeatures.map(lambda features : LabeledPoint(0,features))
spamTraindata = spamFeatures.map(lambda features : LabeledPoint(1,features))

Traindata = hamTraindata.union(spamTraindata)
Traindata.cache()
svm = svm.train(Traindata)

predict_text = []
text = []
data = open('/home/bigdata/phase2.txt','r')
for line in data:
    if line.find('.txt============') == -1:
        text.append(line.strip('\n'))
    else:
        if text:
            predict_text.append(' '.join(text))
            text = []
        else:
            pass
predict_text.append(' '.join(text))

text = sc.parallelize(predict_text)
text = tf.transform(text.map(lambda mail:mail.split(' ')))
text = idfmodel.transform(text)
result = svm.predict(text)
result.repartition(1).saveAsTextFile("file:///home/15182687/output")

