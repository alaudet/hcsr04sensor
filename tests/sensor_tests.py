from nose.tools import *
import math
from hcsr04sensor.sensor import Measurement

TRIG_PIN = 23
ECHO_PIN = 24

def test_measurement():
    '''Assure object is being created properly.'''
    value = Measurement(TRIG_PIN, ECHO_PIN, 20, 'metric', 1)
    assert_equal(isinstance(value, Measurement), True)
    assert_equal(value.trig_pin, TRIG_PIN)
    assert_equal(value.echo_pin, ECHO_PIN)
    assert_equal(value.temperature, 20)
    assert_equal(value.unit, 'metric')
    assert_equal(value.round_to, 1)


def test_imperial_temperature_and_speed_of_sound():
    '''Test that after Fahrenheit is converted to Celsius that speed of sound is
    calculated correctly.'''
    value = Measurement(TRIG_PIN, ECHO_PIN, 68, 'imperial', 1)
    raw_measurement = value.raw_distance()
    speed_of_sound = 331.3 * math.sqrt(1+(value.temperature / 273.15))
    assert_equal(value.temperature, 20.0016)
    assert type(raw_measurement) == float
    assert_equal(speed_of_sound, 343.21555930656075)


def test_imperial_measurements():
    '''Test that an imperial measurement is what you would expect with a precise
    raw_measurement.'''
    value = Measurement(TRIG_PIN, ECHO_PIN, 68, 'imperial', 1)
    raw_measurement = 26.454564846
    hole_depth = 25

    imperial_distance = value.distance_imperial(raw_measurement)
    imperial_depth = value.depth_imperial(raw_measurement, hole_depth)

    assert type(imperial_distance) == float
    assert_equal(imperial_distance, 10.4)
    assert_equal(imperial_depth, 14.6)


def test_metric_measurements():
    '''Test that a metric measurement is what you would expect with a precise
    raw_measurement.'''
    value = Measurement(TRIG_PIN, ECHO_PIN, 20, 'metric', 1)
    raw_measurement = 48.80804985408
    hole_depth = 72

    metric_distance = value.distance_metric(raw_measurement)
    metric_depth = value.depth_metric(raw_measurement, hole_depth)

    assert_equal(metric_distance, 48.8)
    assert_equal(metric_depth, 23.2)


def test_different_sample_size():
    '''Test to ensure that a user defined sample size works correctly.'''
    value = Measurement(TRIG_PIN, ECHO_PIN, 68, 'imperial', 1)
    raw_measurement1 = value.raw_distance(sample_size=1)
    raw_measurement2 = value.raw_distance(sample_size=4)
    raw_measurement3 = value.raw_distance(sample_size=11)
    assert type(raw_measurement1) == float
    assert type(raw_measurement2) == float
    assert type(raw_measurement3) == float
