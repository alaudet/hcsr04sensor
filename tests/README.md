Usage
=====

If using version 0.5.11 of RPi.GPIO you must run tests with sudo

   sudo nosetests -v

If using version 0.6x of RPi.GPIO sudo is no longer required to access the GPIO
on Raspbian Jessie.  Seems to still me needed on Wheezy.  Your mileage may vary.

To use nose on Python3 try the following

    python3 -m "nose" -v

NOTE: You must  adapt your TRIG_PIN and ECHO_PIN setup in sensor_tests

NOTE: If using GPIO.BOARD mode to identify pins ensure you uncomment the proper GPIO_MODE variable.
