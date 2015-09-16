HC-SR04 Ultrasonic Sensor on Raspberry Pi
=========================================

Calculate distance and depth measurements with an HCSR04 Ultrasonic Sound Sensor and a Raspberry Pi.
Instructions assume that you are using Raspbian Linux on your Raspberry Pi.


Python2 Install
===============

Install pip if not on system

    sudo apt-get install python-pip

Install module

    sudo pip install hcsr04sensor


Python3 Install
===============

Install pip if not on system

    sudo apt-get install python3-pip

Install module

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
  increases as sample size is reduced.  For my purposes a sample of 11 readings gives a consistent
  value that I can trust and takes approximately 5 seconds to run.

  This module uses BCM pin values on the Pi.  See the Raspberry Pi pin layout documentation for your model.

* Rounds the value to a specified decimal place.

* Adjusts the reading based on temperature by adjusting the speed of sound.

* Allows measuring distance and depth in metric and imperial units.  See;

    pydoc hcsr04sensor.sensor


Accuracy of Readings
====================

If you need highly accurate readings then this module would not be suitable for your project.  In that case you should probably use an Arduino instead of a Raspberry Pi.

Linux is not a Real Time OS so you can expect to get a small variance on each reading, usually within a half cm of the actual value.  I say "usually" because every once in a while you can get a reading that is way out of range.  This is due to the OS executing other tasks before getting your distance reading.  It is why I use a sample of readings.  I can always trust that the median of my sample of 11 readings is good.

Highly accurate readings are not required for some applications, for example I use this module in an application I wrote for a sump pump monitor.  I am not worried about millimeter accuracy for that application.  1 cm variance on a meter deep pit is close enough to alert me to problems.

Usage
=====

See example scripts in https://github.com/alaudet/hcsr04sensor/tree/master/examples.

Access to Raspberry Pi GPIO pins require elevated priviledges.  Run example
scripts with sudo.
