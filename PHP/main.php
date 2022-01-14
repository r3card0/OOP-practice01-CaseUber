<?php

require_once('Car.php');
require_once('Account.php');

$car = new Car('KILL007', new Account('James Bond','GUN123'));
$car->PrintDataCar();

echo "\n";