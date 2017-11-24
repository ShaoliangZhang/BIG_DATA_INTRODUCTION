import os
from os.path import join
import numpy as np
dest = "/Users/tank/Downloads/train/"
output = open('output.txt','w')
mail = []
target = []
for root, dirs, files in os.walk( dest ):
    for OneFileName in files :
        try:
            if OneFileName.find( '.txt' ) == -1 :
                continue
            if OneFileName.find('ham')  != -1:
                target.append(0)
            elif OneFileName.find('spam') != -1:
                target.append(1)
            OneFullFileName = join( root, OneFileName )#path of one file
            file = []
            for line in open(OneFullFileName,'r',encoding = 'latin1'):
                file.append(line)
            file =''.join(file)
            mail.append(file)
        except:
            print(OneFileName)
            if target:
                target.pop()
            else:
                pass
print('data load success')

from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn import grid_search
from sklearn.feature_extraction.text import CountVectorizer

extractor = CountVectorizer()

parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svr = SVC()
grid = grid_search.GridSearchCV(svr, parameters)

pipeline = Pipeline([('feature_extraction', extractor),
                      ('clf', grid)
                     ])

#scores = cross_val_score(pipeline, mail, target,
#scoring='accuracy')
#print(np.mean(scores))

predict_text = []
text = []
data = open('/Users/tank/Downloads/phase1.txt','r',encoding = 'latin1')
for line in data:
    if line.find('.txt============') == -1:
        text.append(line)
    else:
        if text:
            predict_text.append(''.join(text))
            text.clear()
        else:
            pass
predict_text.append(''.join(text))
svmclf=pipeline.fit(mail,target)
n = 0
s = 0
h = 0
for text in predict_text:
    n = n+1
    result = svmclf.predict([text])
    if result == [0]:
        output.write('0\n')
        h = h + 1
    elif result == [1]:
        output.write('1\n')
        s = s + 1
    else:
        print('error in text: ',n)
output.close()
print(n)
