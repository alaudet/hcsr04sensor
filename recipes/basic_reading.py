'''Example of getting a direct reading from RPi.GPIO.'''

import RPi.GPIO as GPIO
from hcsr04sensor import sensor

# This script uses a static function outside of the Measurement class
# in hcsr04sensor named basic_distance
# No median readings pulled from a sample for error correction
# No exception handling for faulty cable
# No pin cleanups.  You handle all of these things in your own code
# Just a simple return of a cm distance as reported directly from Rpi.GPIO

trig = 17
echo = 27
gpio_mode = GPIO.BCM # use GPIO.BOARD for board pin values
temp = -30  #default is standard room temp (20Celcius)

distance_warm = sensor.basic_distance(trig, echo, gpio_mode)

# example of passing temperature reading
# temperature affects speed of sound
# Easily combine with a temperature sensor to pass the current temp

distance_cold = sensor.basic_distance(trig, echo, gpio_mode, celsius=temp)

print("The distance at  20 Celsius is {} cm's".format(distance_warm))
print("The distance at -30 Celsius is {} cm's".format(distance_cold))
# cleanup gpio pins.
GPIO.cleanup((trig, echo))
