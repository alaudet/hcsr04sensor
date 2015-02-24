HC-SR04 Ultrasonic Sensor on Raspberry Pi
=========================================

A simple module for calculating distance and depth measurements with an HCSR04 Ultrasonic Sound Sensor and a Raspberry Pi.


Install
=======

    sudo pip install hcsr04sensor

Description
===========
The module does the following;

* Returns an error corrected distance by using the median reading of a sorted
  sample.  

* Rounds the value to a specified decimal place.

* Adjusts the reading based on temperature by adjusting the speed of sound.

* Allows measuring distance and depth in metric and imperial units.  See;

    pydoc hcsr04sensor.sensor

Usage
=====

See example scripts in https://github.com/alaudet/hcsr04sensor/tree/master/examples.

Access to Raspberry Pi GPIO pins require elevated priviledges.  Run example
scripts with sudo.
