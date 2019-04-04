#!/usr/bin/python3
#Script start from here

#Load Classifier from disk
import pickle
loaded_clf = pickle.load(open("nbMovie2.sav", 'rb'))

#Handle Parameters sending from php
import sys
param_1= sys.argv[1]
param_2= sys.argv[2]

#Make predict in terms of given parameters based on fit classifier
y_pred = loaded_clf.predict([[int(param_1), int(param_2)]])
print ('The Genre is ')
print (''.join(y_pred))