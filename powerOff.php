<?php 
$argument1 = $_GET['arg1'];
exec("sudo python /home/pi/powerOff.py $argument1");
