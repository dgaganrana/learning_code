<?php
/*
* Different way to push data into array in PHP
*/

//Declare array
// $array_name = array(); // This was the conventional method of array declaration
$array_name = [];

// Push elements to array
$array_name[] = 'One';
$array_name[] = 'two';

// Alternative way to push elements to array using push function
array_push($array_name, 'array_element');
?>
