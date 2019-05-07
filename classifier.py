#!/usr/bin/python3
#Script start from here

#Access to mySQL search database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  passwd="password",
  database="table"
)

#Convert SQL to Pandas Data structure
import pandas as pd
import numpy as np

df = pd.read_sql('SELECT Genre1, Budget, Revenue FROM movie2 WHERE Budget <> "" and Revenue <> "" and Genre1 <> ""', con=mydb)
#print (df.shape)
#print (df.head(n=100))

#Preprocess data
X = df.drop('Genre1', axis=1)
y = df['Genre1']
#print (X)
#print (y)

#Split data into training part and testing part
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10)
#print ("X_test is " + str(X_test))
#print ("y_test is " + str(y_test))

#Train data to built Naive Bayes Classifier
from sklearn.naive_bayes import GaussianNB
nbClassifier = GaussianNB()
nbClassifier.fit (X_train, y_train)

#Make predictions for test data
y_pred = nbClassifier.predict(X_test)

#Evaluating the algorithm
from sklearn import metrics
print ('Accuracy: ')
print(metrics.accuracy_score(y_test, y_pred))

from sklearn.metrics import classification_report
print ('Report: ')
print(classification_report(y_test, y_pred)) 

#Save fit classifier as a file for future use
import pickle
nbMovie2_file = "nbMovie2.sav"
pickle.dump(nbClassifier, open(nbMovie2_file, 'wb'))
print ("Model successfully trained, saved as file 'nbMovie2.sav' in root directory")