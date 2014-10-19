#!/usr/bin/python

import hcsr04sensor.sensor as sensor


def depth(hole_depth):
    '''measure the distance in cm's and return a rounded float'''
    trig_pin = 17
    echo_pin = 27
    rounded_to = 1
    temperature = 20
    value = sensor.Measurement(trig_pin, echo_pin, rounded_to, temperature)
    distance = value.distance()
    return hole_depth - distance
 
if __name__ == "__main__":
    hole_depth = 89.7
    level = depth(float(hole_depth))
    print "Liquid Depth = {} centimeters.".format(round(level, 1))
