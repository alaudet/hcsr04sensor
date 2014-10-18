#!/usr/bin/python

import hcsr04sensor.pihcsr04 as sensor


def distance():
    '''measure the distance in cm's and return a rounded float'''
    trig_pin = 17
    echo_pin = 27
    rounded_to = 1
    temperature = 20
    value = sensor.Measurement(trig_pin, echo_pin, rounded_to, temperature)
    return value.distance()

if __name__ == "__main__":
    distance = distance()
    print "The measured distance is {} centimeters".format(distance)
