# HC-SR04 Ultrasonic Sensor on Raspberry Pi

[Hcsr04sensor Web Page](https://www.linuxnorth.org/hcsr04sensor)

Calculate distance and depth measurements with an HCSR04 Ultrasonic Sound Sensor and a Raspberry Pi. Instructions assume that you are using Raspbian Linux.

This module also works with the JSN-SR04T waterproof sound sensor.

![wiring](https://www.linuxnorth.org/raspi-sump/images/raspi-sump-wiring.jpg)

## Python3 Install

Install dependencies;

    sudo apt install python3-pip python3-rpi.gpio

The above installs RPi.GPIO 0.7.0.  If using Raspberry Pi OS (Bullseye) you may prefer to install RPi.GPIO 0.7.1 with Pip. Either one should work.

 To get the latest install it with Pip as follows;

    sudo apt remove python3-rpi.gpio  <--0.7.0
    sudo pip3 install RPi.GPIO <--0.7.1

Install the hcsr04sensor module

    sudo pip3 install hcsr04sensor

## Description

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

* Uses BCM pin values by default.  BOARD pin values are supported.

* Adjusts the reading based on temperature by adjusting the speed of sound.

* Allows measuring distance and depth in metric and imperial units.  See;

    pydoc hcsr04sensor.sensor

* Raises an exception if a faulty cable or sensor prevents an echo pulse from being received.

* Calculate the volume of different types of containers.  See recipes for examples.

## Accuracy of Readings

If you need highly accurate readings then this module would not be suitable for your project.  In that case you should probably use an Arduino instead of a Raspberry Pi.

Linux is not a Real Time OS so you can expect to get a small variance on each reading, usually within a half cm of the actual value.  I say "usually" because every once in a while you can get a reading that is way out of range.  This is due to the OS executing other tasks before getting your distance reading.  It is why I use a sample of readings.  I can always trust that the median of my sample of 11 readings is good.

Highly accurate readings are not required for some applications. For example I use this module in an application I wrote for a sump pump monitor.  I am not worried about millimeter accuracy for that application.  1 cm variance on a meter deep pit is close enough to alert me to problems.

Another example would be to calculate the water volume of a drinking water well (standing cylinder shape).
It would not matter if you are a gallon off on a 1000 gallon reading.


## Distance Limitations

The HCSR04 sensor is suited for short distance readings.  The specification manual says it is suitable up to 13 feet.  I have tested it to go further than that, but anything over 12 feet starts having periodic strange readings.
This module is not suitable for long distances.


## Usage

See example scripts in https://github.com/alaudet/hcsr04sensor/tree/master/recipes

Access to Raspberry Pi GPIO pins requires the user account to be in the Linux gpio group.

To add your user account name to the gpio group;

    sudo usermod -aG gpio username

## Testing the Module

Added a script that is installed to /usr/local/bin called hcsr04.py.
This utility does not presently support BOARD pin values.  Use BCM pin values.

usage: hcsr04.py [-h] -t TRIG -e ECHO [-sp SPEED] [-ss SAMPLES]

## Take a Basic Reading

If you don't want to use a sample of readings for error handling, warnings or pin cleanups I have included a static method in the Measurement class that will return a basic metric reading.  It returns the exact one-time reading that is provided  by the sensor and RPi.GPIO.  This allows you to handle all of these things to your own preference in your code.

See the example basic_reading.py script in https://github.com/alaudet/hcsr04sensor/tree/master/recipes


## Contributing

Read the contributing guidelines if you are interested in collaborating on this project.


## Donate

[Your Donation is Appreciated](https://www.linuxnorth.org/donate/)
