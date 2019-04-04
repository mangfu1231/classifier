# Classifier
A Naive Bayes Classifier for movie genre based on budget and revenue.

## Overview
Movie genre is relavant to budget and revenue. Given these two numbers, we sometimes are able to make reasonable inference for the genre of a movie. Influenced by this matter of fact, we developed a classifier based on budget and revenue. The classifier consists of five separate scripts. Two of them are for the purpose of training. The other three is for classifying by user given budget and revenue.

## Scripts in detail
- train.php
Since this app is depended on LAMP, runing python directly on Apache is not a good choice. Train.php calls the python script to run which is similiar to run python through bash.
```php
$command = escapeshellcmd('./classifier.py');
$output = shell_exec($command);
echo $output;
```
- classifier.py
This is the main script for training classifier model. We connected mySQL databse, read dataset into pandas dataframe, seperate them by drop method as label and features. And we divided the dataset into training and testing datasets. Sklearn module was applied to train and eveluate the classifier. We also save the trained model as a file for future use.
```python
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="chaoweiw_search"
)
```
```python
df = pd.read_sql('SELECT Genre1, Budget, Revenue FROM movie2 WHERE Budget <> "" and Revenue <> "" and Genre1 <> ""', con=mydb)
X = df.drop('Genre1', axis=1)
y = df['Genre1']
```
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10)
from sklearn.naive_bayes import GaussianNB
nbClassifier = GaussianNB()
nbClassifier.fit (X_train, y_train)
y_pred = nbClassifier.predict(X_test)
from sklearn import metrics
print ('Accuracy: ')
print(metrics.accuracy_score(y_test, y_pred))
from sklearn.metrics import classification_report
print ('Report: ')
print(classification_report(y_test, y_pred)) 
```
```python
import pickle
nbMovie2_file = "nbMovie2.sav"
pickle.dump(nbClassifier, open(nbMovie2_file, 'wb'))
print ("Model successfully trained, saved as file 'nbMovie2.sav' in root directory")
```
- classifier.html
The script is nothing more than a basic user interface for input.
```html
  <form class="search" action="classifier.php" method="get" style="margin:auto;max-width:300px">
    <input type="number" placeholder="please type in budget" name="budget">
    <input type="number" placeholder="please type in revenue" name="revenue">
    <button type="submit" name="search">Submit</button>
  </form>
```
- classifier.php
The php will handle user input and call another python script to run trained classifier.
```php
$input = array($_GET["budget"], $_GET["revenue"]);
$command = escapeshellcmd('./nbMovie2.py ' . $_GET["budget"] . ' ' . $_GET["revenue"]);
$output = shell_exec($command);
echo $output;
```
- nbMovie2.py
The script run the trained classifier (nbMovie2.sav), pass user input to the classifier and return genre result according to the two numbers given by user.
```python
loaded_clf = pickle.load(open("nbMovie2.sav", 'rb'))
import sys
param_1= sys.argv[1]
param_2= sys.argv[2]
y_pred = loaded_clf.predict([[int(param_1), int(param_2)]])
print ('The Genre is ')
print (''.join(y_pred))
```
## Methodology on blog
https://chaoweiwang6.wixsite.com/website/post/how-to-create-synergy-in-the-workplace
