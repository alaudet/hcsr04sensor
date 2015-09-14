HC-SR04 Ultrasonic Sensor on Raspberry Pi
=========================================

A simple module for calculating distance and depth measurements with an HCSR04 Ultrasonic Sound Sensor and a Raspberry Pi.

Install pip if not on system
============================

If using Python2   sudo apt-get install python-pip

If using Python3   sudo apt-get install python3-pip


Python2 Install
===============

    sudo pip install hcsr04sensor

Python3 Install
===============

    sudo pip-3.2 install hcsr04sensor

Description
===========
The module does the following;

* Returns an error corrected distance by using the median reading of a sorted
  sample. NOTE - The default sample size is 11 readings.  

  You can specify a
  different sample size by passing sample_size=x  to raw_distance (where x is your desired
  number of readings).  This is useful if you need to lower the sample size to take
  quicker readings.  Beware that the probability of getting erroneous readings
  increases as sample size is reduced.

* Rounds the value to a specified decimal place.

* Adjusts the reading based on temperature by adjusting the speed of sound.

* Allows measuring distance and depth in metric and imperial units.  See;

    pydoc hcsr04sensor.sensor

Usage
=====

See example scripts in https://github.com/alaudet/hcsr04sensor/tree/master/examples.

Access to Raspberry Pi GPIO pins require elevated priviledges.  Run example
scripts with sudo.
