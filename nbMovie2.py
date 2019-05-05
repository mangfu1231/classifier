#!/usr/bin/python3
#Script start from here

#Load Classifier from disk
import pickle
loaded_clf = pickle.load(open("nbMovie2.sav", 'rb'))

#Handle Parameters sending from php
import sys
param_1 = sys.argv[1]
param_2 = sys.argv[2]
user_input = [[int(param_1), int(param_2)]]

#Make predict in terms of given parameters based on fit classifier
y_pred = loaded_clf.predict(user_input)

#Sort probability for genres
prob = loaded_clf.predict_proba(user_input)
prob.sort()

#Output the genre with the highest probability and the probability value
print ('The Genre is ')
print (''.join(y_pred))

print ('. The probability for this genre is ')
print (prob[0][18])
print ('.')