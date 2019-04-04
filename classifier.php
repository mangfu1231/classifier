<!DOCTYPE html>

<html>
  <head>
    <title>Result page</title>
  </head>

  <body>
    <a href="classifier.html" style="text-decoration: none"><button style="display: block;">Go Back</button></a>
  </body>
</html>

<?php 

//Form data handling
$input = array($_GET["budget"], $_GET["revenue"]);
//Execute python script
$command = escapeshellcmd('./nbMovie2.py ' . $_GET["budget"] . ' ' . $_GET["revenue"]);
$output = shell_exec($command);
echo $output;

?>