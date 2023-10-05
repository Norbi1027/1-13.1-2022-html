<?php

$sname= "localhost";
$unmae= "root";
$password = "";

$db_name = "php-crud";

$conn1 = mysqli_connect($sname, $unmae, $password, $db_name);

if (!$conn1) {
	echo "Connection failed!";
}