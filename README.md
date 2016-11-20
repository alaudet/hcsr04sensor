HC-SR04 Ultrasonic Sensor on Raspberry Pi
=========================================

Calculate distance and depth measurements with an HCSR04 Ultrasonic Sound Sensor and a Raspberry Pi.
Instructions assume that you are using Raspbian Linux.


Python2 Install
===============


    sudo apt-get install python-pip
    sudo pip install hcsr04sensor


Python3 Install
===============


    sudo apt-get install python3-pip
    sudo pip3 install hcsr04sensor


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
  value that I can trust and takes approximately 3 seconds to run with a 0.1
  second wait time between individual samples.

  It is also possible to speed up the readings by passing a lower value to
  sample_wait in raw_distance.   

  The lower the value the quicker the invidual
  samples will be taken.  A default of 0.1 is a safe wait time but this can be
  reduced further.  CPU usage increases as faster readings are taken as well as
  the chance for errors.
  
  This module uses BCM pin values.  See the Raspberry Pi pin layout documentation for your model.

* Rounds the value to a specified decimal place.

* Adjusts the reading based on temperature by adjusting the speed of sound.

* Allows measuring distance and depth in metric and imperial units.  See;

    pydoc hcsr04sensor.sensor

* Raises an exception if a faulty cable or sensor prevents an echo pulse from being received.

Accuracy of Readings
====================

If you need highly accurate readings then this module would not be suitable for your project.  In that case you should probably use an Arduino instead of a Raspberry Pi.

Linux is not a Real Time OS so you can expect to get a small variance on each reading, usually within a half cm of the actual value.  I say "usually" because every once in a while you can get a reading that is way out of range.  This is due to the OS executing other tasks before getting your distance reading.  It is why I use a sample of readings.  I can always trust that the median of my sample of 11 readings is good.

Highly accurate readings are not required for some applications, for example I use this module in an application I wrote for a sump pump monitor.  I am not worried about millimeter accuracy for that application.  1 cm variance on a meter deep pit is close enough to alert me to problems.


Distance Limitations
====================

The HCSR04 sensor is suited for short distance readings.  The specification manual says it is suitable up to 13 feet.  I have tested it to go further than that, but anything over 12 feet starts having periodic strange readings.
This module is not suitable for long distances. 


Usage
=====

See example scripts in https://github.com/alaudet/hcsr04sensor/tree/master/examples.

Access to Raspberry Pi GPIO pins require elevated priviledges if using version 0.5.11 of RPi.GPIO.  Run example
scripts with sudo.

Recommended
===========

To upgrade to version 0.6.x of RPi.GPIO which does not require elevated priviledges you can simply upgrade as follows;

Note: On Raspbian Wheezy you still seem to have to run RPi.GPIO with sudo in version 6.  It works without sudo in 
Rasbian Jessie which is the latest version of Raspbian.

For Python 2

    sudo pip install -U hcsr04sensor

or

    sudo apt-get upgrade python-rpi.gpio




For Python 3

    sudo pip3 install -U hcsr04sensor

or

    sudo apt-get upgrade python3-rpi.gpio

Contributing
============

Contributions to hcsr04sensor are welcome.  Please open an issue in the issue
tracker prior to a pull request.

New features and bug fixes should be applied against the devel branch and not master. Contributions against the master branch will be rejected.

Nose is currently used for testing.  All tests should pass before issuing
the pull request.
