# classifier
A Naive Bayes Classifier for movie genre based on budget and revenue.

## Overview
Movie genre is relavant to budget and revenue. Given these two numbers, we sometimes are able to make reasonable inference for the genre of a movie. Influenced by this matter of fact, we developed a classifier based on budget and revenue. The classifier consists of five separate scripts. Two of them are for the purpose of training. The other three is for classifying by user given budget and revenue.

## Script in detail
- train.php
Since this app is depended on LAMP, runing python directly on Apache is not a good choice. Train.php calls the python script to run which is similiar to run python through bash.
```php
$command = escapeshellcmd('./classifier.py');
$output = shell_exec($command);
echo $output;
```


- classifier.html
The script is nothing more than a webpage. 
