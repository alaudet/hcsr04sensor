from nose.tools import *
import math
import RPi.GPIO as GPIO
from hcsr04sensor.sensor import Measurement, basic_distance

TRIG_PIN = 17
ECHO_PIN = 27

# Uncomment the mode you are using to identify the GPIO pins.  Default is BCM
GPIO_MODE = GPIO.BCM
# GPIO_MODE = GPIO.BOARD


def raw_distance():
    value = Measurement(TRIG_PIN, ECHO_PIN)
    return value.raw_distance()


def test_measurement():
    """Test that object is being created properly."""
    value = Measurement(TRIG_PIN, ECHO_PIN, 25, "metric", 2, gpio_mode=GPIO_MODE)
    value_defaults = Measurement(TRIG_PIN, ECHO_PIN)
    assert_equal(isinstance(value, Measurement), True)
    assert_equal(value.trig_pin, TRIG_PIN)
    assert_equal(value.echo_pin, ECHO_PIN)
    assert_equal(value.temperature, 25)
    assert_equal(value.unit, "metric")
    assert_equal(value.round_to, 2)
    assert_equal(value_defaults.trig_pin, TRIG_PIN)
    assert_equal(value_defaults.echo_pin, ECHO_PIN)
    assert_equal(value_defaults.temperature, 20)
    assert_equal(value_defaults.unit, "metric")
    assert_equal(value_defaults.round_to, 1)


def test_imperial_temperature_and_speed_of_sound():
    """Test that after Fahrenheit is converted to Celsius, that speed of sound is
    calculated correctly."""
    value = Measurement(TRIG_PIN, ECHO_PIN, 68, "imperial", gpio_mode=GPIO_MODE)
    raw_measurement = value.raw_distance()
    speed_of_sound = 331.3 * math.sqrt(1 + (value.temperature / 273.15))
    assert_equal(value.temperature, 20.0016)
    assert_equal(value.unit, "imperial")
    assert_equal(value.round_to, 1)
    assert type(raw_measurement) == float
    assert_equal(speed_of_sound, 343.21555930656075)


def test_imperial_measurements():
    """Test that an imperial measurement is what you would expect with a precise
    raw_measurement."""
    value = Measurement(TRIG_PIN, ECHO_PIN, 68, "imperial", gpio_mode=GPIO_MODE)
    raw_measurement = 26.454564846
    hole_depth = 25

    imperial_distance = value.distance_imperial(raw_measurement)
    imperial_depth = value.depth_imperial(raw_measurement, hole_depth)

    assert type(imperial_distance) == float
    assert_equal(imperial_distance, 10.4)
    assert_equal(imperial_depth, 14.6)


def test_metric_measurements():
    """Test that a metric measurement is what you would expect with a precise
    raw_measurement."""
    value = Measurement(TRIG_PIN, ECHO_PIN, 20, "metric", 2, gpio_mode=GPIO_MODE)
    value_defaults = Measurement(TRIG_PIN, ECHO_PIN)
    raw_measurement = 48.80804985408
    hole_depth = 72

    metric_distance = value.distance_metric(raw_measurement)
    metric_depth = value.depth_metric(raw_measurement, hole_depth)

    assert_equal(metric_distance, 48.81)
    assert_equal(metric_depth, 23.19)

    metric_distance = value_defaults.distance_metric(raw_measurement)
    metric_depth = value_defaults.depth_metric(raw_measurement, hole_depth)

    assert_equal(metric_distance, 48.8)
    assert_equal(metric_depth, 23.2)


def test_different_sample_size():
    """Test that a user defined sample_size works correctly."""
    value = Measurement(TRIG_PIN, ECHO_PIN, 68, "imperial", 1, gpio_mode=GPIO_MODE)
    raw_measurement1 = value.raw_distance(sample_size=1)
    raw_measurement2 = value.raw_distance(sample_size=4)
    raw_measurement3 = value.raw_distance(sample_size=11)
    assert type(raw_measurement1) == float
    assert type(raw_measurement2) == float
    assert type(raw_measurement3) == float


def test_different_sample_wait():
    """Test that a user defined sample_wait time work correctly."""
    value = Measurement(TRIG_PIN, ECHO_PIN, gpio_mode=GPIO_MODE)
    raw_measurement1 = value.raw_distance(sample_wait=0.3)
    raw_measurement2 = value.raw_distance(sample_wait=0.1)
    raw_measurement3 = value.raw_distance(sample_wait=0.03)
    raw_measurement4 = value.raw_distance(sample_wait=0.01)
    assert type(raw_measurement1) == float
    assert type(raw_measurement2) == float
    assert type(raw_measurement3) == float
    assert type(raw_measurement4) == float


def test_basic_distancei_bcm():
    """Test that float returned with default, positive and negative temps"""
    GPIO.setmode(GPIO.BCM)
    basic_reading = basic_distance(TRIG_PIN, ECHO_PIN)
    basic_reading2 = basic_distance(TRIG_PIN, ECHO_PIN, celsius=10)
    basic_reading3 = basic_distance(TRIG_PIN, ECHO_PIN, celsius=0)
    basic_reading4 = basic_distance(TRIG_PIN, ECHO_PIN, celsius=-100)
    assert type(basic_reading) == float
    assert type(basic_reading2) == float
    assert type(basic_reading3) == float
    assert type(basic_reading4) == float
    GPIO.cleanup((TRIG_PIN, ECHO_PIN))


def test_raises_exception_unit():
    """Test that a ValueError is raised if user passes invalid unit type"""
    value = Measurement(TRIG_PIN, ECHO_PIN, unit="Fahrenheit")
    assert_raises(ValueError, value.raw_distance)


def test_raises_exception_no_pulse():
    """Test that SystemError raised if echo pulse not received.
       Using the wrong echo pin but typically this error gets raised
       with a faulty cable.  Wrong echo pin simulates that condition"""
    wrong_echo_pin = ECHO_PIN - 1
    value = Measurement(TRIG_PIN, wrong_echo_pin)
    assert_raises(SystemError, value.raw_distance)


def test_depth():
    pass


def test_distance():
    pass


def test_cylinder_volume_side():
    pass


def test_cylinder_volume_standing():
    pass


def test_box_volume():
    pass
