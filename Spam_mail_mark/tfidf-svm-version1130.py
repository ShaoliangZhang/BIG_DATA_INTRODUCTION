#!/usr/bin/python
# -*- coding:latin1-
from pyspark import SparkContext
sc = SparkContext()

import os
from os.path import join
import numpy as np
dest = "/usr/homework/train/"
output = open('sparkoutput.txt','w')
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
from pyspark.mllib.classification import LogisticRegressionWithSGD,SVMWithSGD
lrlearner = LogisticRegressionWithSGD()
svm = SVMWithSGD()

from pyspark.mllib.feature import HashingTF,IDF
tf = HashingTF(numFeatures = 80000)
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
ll = lrlearner.train(Traindata)
svm = svm.train(Traindata)

predict_text = []
text = []
data = open('phase1.txt','r')
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

n = 0
s = 0
h = 0
for text in predict_text:
    n = n+1
    text = tf.transform(text.split(' '))
    text = idfmodel.transform(text)
    result = svm.predict(text)
    if result == 0:
        output.write('0\n')
        h = h + 1
    elif result == 1:
        output.write('1\n')
        s = s + 1
    else:
        print('error in text: ',n)
output.close()
print s
print h

