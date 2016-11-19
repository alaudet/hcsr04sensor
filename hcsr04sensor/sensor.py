'''Measure the distance or depth with an HCSR04 Ultrasonic sound 
sensor and a Raspberry Pi.  Imperial and Metric measurements are available'''

# Al Audet
# MIT License

import time
import math
import RPi.GPIO as GPIO


class Measurement(object):
    '''Create a measurement using a HC-SR04 Ultrasonic Sensor connected to 
    the GPIO pins of a Raspberry Pi.

    Metric values are used by default. For imperial values use
    unit='imperial'
    temperature=<Desired temperature in Fahrenheit>
    '''

    def __init__(self,
                 trig_pin,
                 echo_pin,
                 temperature=20,
                 unit='metric',
                 round_to=1
                 ):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.temperature = temperature
        self.unit = unit
        self.round_to = round_to

    def raw_distance(self, sample_size=11, sample_wait=0.1):
        '''Return an error corrected unrounded distance, in cm, of an object 
        adjusted for temperature in Celcius.  The distance calculated
        is the median value of a sample of `sample_size` readings.

        
        Speed of readings is a result of two variables.  The sample_size
        per reading and the sample_wait (interval between individual samples).

        Example: To use a sample size of 5 instead of 11 will increase the 
        speed of your reading but could increase variance in readings;

        value = sensor.Measurement(trig_pin, echo_pin)
        r = value.raw_distance(sample_size=5)
        
        Adjusting the interval between individual samples can also
        increase the speed of the reading.  Increasing the speed will also
        increase CPU usage.  Setting it too low will cause errors.  A default
        of sample_wait=0.1 is a good balance between speed and minimizing 
        CPU usage.  It is also a safe setting that should not cause errors.
        
        e.g.

        r = value.raw_distance(sample_wait=0.03)
        '''

        if self.unit == 'imperial':
            self.temperature = (self.temperature - 32) * 0.5556
        elif self.unit == 'metric':
            pass
        else:
            raise ValueError(
                'Wrong Unit Type. Unit Must be imperial or metric')

        speed_of_sound = 331.3 * math.sqrt(1+(self.temperature / 273.15))
        sample = []
        # setup input/output pins
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        
        for distance_reading in range(sample_size):
            GPIO.output(self.trig_pin, GPIO.LOW)
            time.sleep(sample_wait)
            GPIO.output(self.trig_pin, True)
            time.sleep(0.00001)
            GPIO.output(self.trig_pin, False)
            echo_status_counter = 1
            while GPIO.input(self.echo_pin) == 0:
                if echo_status_counter < 1000:
                    sonar_signal_off = time.time()
                    echo_status_counter += 1
                else:
                    raise SystemError('Echo pulse was not received')
            while GPIO.input(self.echo_pin) == 1:
                sonar_signal_on = time.time()
            time_passed = sonar_signal_on - sonar_signal_off
            distance_cm = time_passed * ((speed_of_sound * 100) / 2)
            sample.append(distance_cm)
        sorted_sample = sorted(sample)
        # Only cleanup the pins used to prevent clobbering
        # any others in use by the program
        GPIO.cleanup((self.trig_pin, self.echo_pin))
        return sorted_sample[sample_size // 2]

    def depth_metric(self, median_reading, hole_depth):
        '''Calculate the rounded metric depth of a liquid. hole_depth is the
        distance, in cm's, from the sensor to the bottom of the hole.'''
        return round(hole_depth - median_reading, self.round_to)

    def depth_imperial(self, median_reading, hole_depth):
        '''Calculate the rounded imperial depth of a liquid. hole_depth is the
        distance, in inches, from the sensor to the bottom of the hole.'''
        return round(hole_depth - (median_reading * 0.394), self.round_to)

    def distance_metric(self, median_reading):
        '''Calculate the rounded metric distance, in cm's, from the sensor
        to an object'''
        return round(median_reading, self.round_to)

    def distance_imperial(self, median_reading):
        '''Calculate the rounded imperial distance, in inches, from the sensor
        to an oject.'''
        return round(median_reading * 0.394, self.round_to)
