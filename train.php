<?php 

//Execute python script
$command = escapeshellcmd('./classifier.py');
$output = shell_exec($command);
echo $output;

?>
