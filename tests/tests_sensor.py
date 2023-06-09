import unittest
import math
import RPi.GPIO as GPIO
from hcsr04sensor.sensor import Measurement

TRIG_PIN = 17
ECHO_PIN = 27

# Uncomment the mode you are using to identify the GPIO pins.  Default is BCM
GPIO_MODE = GPIO.BCM
# GPIO_MODE = GPIO.BOARD


class MeasurementTestCase(unittest.TestCase):
    def setUp(self):
        self.mode = GPIO.setmode(GPIO_MODE)
        self.metric_value_25 = Measurement(
            TRIG_PIN, ECHO_PIN, 25, "metric", gpio_mode=GPIO_MODE
        )
        self.imperial_value = Measurement(TRIG_PIN, ECHO_PIN, 68, "imperial", GPIO_MODE)
        self.metric_value = Measurement(TRIG_PIN, ECHO_PIN, 20, "metric", GPIO_MODE)

    def tearDown(self):
        pass

    def test_measurement(self):
        """Test that object is being created properly."""
        value = self.metric_value_25
        value_defaults = Measurement(TRIG_PIN, ECHO_PIN)
        self.assertIsInstance(value, Measurement)
        self.assertEqual(value.trig_pin, TRIG_PIN)
        self.assertEqual(value.echo_pin, ECHO_PIN)
        self.assertEqual(value.temperature, 25)
        self.assertEqual(value.unit, "metric")
        self.assertEqual(value_defaults.trig_pin, TRIG_PIN)
        self.assertEqual(value_defaults.echo_pin, ECHO_PIN)
        self.assertEqual(value_defaults.temperature, 20)
        self.assertEqual(value_defaults.unit, "metric")

    def test_imperial_temperature_and_speed_of_sound(self):
        """Test that after Fahrenheit is converted to Celsius, that speed of sound is
        calculated correctly."""
        value = self.imperial_value
        raw_measurement = value.raw_distance()
        speed_of_sound = 331.3 * math.sqrt(1 + (value.temperature / 273.15))
        self.assertAlmostEqual(value.temperature, 20.0016)
        self.assertEqual(value.unit, "imperial")
        self.assertIsInstance(raw_measurement, float)
        self.assertAlmostEqual(speed_of_sound, 343.21555930656075)

    def test_imperial_measurements(self):
        """Test that an imperial measurement is what you would expect with a precise
        raw_measurement."""
        value = self.imperial_value
        raw_measurement = 26.454564846
        hole_depth = 25

        imperial_distance = value.distance(raw_measurement)
        imperial_depth = value.depth(raw_measurement, hole_depth)

        self.assertIsInstance(imperial_distance, float)
        self.assertAlmostEqual(imperial_distance, 10.423098549324001)
        self.assertAlmostEqual(imperial_depth, 14.576901450675999)

    def test_metric_measurements(self):
        """Test that a metric measurement is what you would expect with a precise
        raw_measurement."""
        value = self.metric_value
        raw_measurement = 48.80804985408
        hole_depth = 72

        metric_distance = value.distance(raw_measurement)
        metric_depth = value.depth(raw_measurement, hole_depth)

        self.assertAlmostEqual(metric_distance, 48.80804985408)
        self.assertAlmostEqual(metric_depth, 23.191950145920003)

    def test_different_sample_size(self):
        """Test that a user defined sample_size works correctly."""
        value = self.imperial_value
        raw_measurement1 = value.raw_distance(sample_size=1)
        raw_measurement2 = value.raw_distance(sample_size=4)
        raw_measurement3 = value.raw_distance(sample_size=11)
        self.assertIsInstance(raw_measurement1, float)
        self.assertIsInstance(raw_measurement2, float)
        self.assertIsInstance(raw_measurement3, float)

    def test_different_sample_wait(self):
        """Test that a user defined sample_wait time works correctly."""
        value = self.metric_value
        raw_measurement1 = value.raw_distance(sample_wait=0.3)
        raw_measurement2 = value.raw_distance(sample_wait=0.1)
        raw_measurement3 = value.raw_distance(sample_wait=0.03)
        raw_measurement4 = value.raw_distance(sample_wait=0.01)
        self.assertIsInstance(raw_measurement1, float)
        self.assertIsInstance(raw_measurement2, float)
        self.assertIsInstance(raw_measurement3, float)
        self.assertIsInstance(raw_measurement4, float)

    def test_basic_distance_bcm(self):
        """Test static method ensuring a float is returned with default,
        positive, and negative temps."""
        self.mode
        GPIO.setwarnings(False)
        x = Measurement
        basic_reading = x.basic_distance(TRIG_PIN, ECHO_PIN)
        basic_reading2 = x.basic_distance(TRIG_PIN, ECHO_PIN, celsius=10)
        basic_reading3 = x.basic_distance(TRIG_PIN, ECHO_PIN, celsius=0)
        basic_reading4 = x.basic_distance(TRIG_PIN, ECHO_PIN, celsius=-100)
        self.assertIsInstance(basic_reading, float)
        self.assertIsInstance(basic_reading2, float)
        self.assertIsInstance(basic_reading3, float)
        self.assertIsInstance(basic_reading4, float)
        GPIO.cleanup((TRIG_PIN, ECHO_PIN))

    def test_raises_exception_unit(self):
        """Test that a ValueError is raised if user passes invalid unit type"""
        with self.assertRaises(ValueError):
            Measurement(TRIG_PIN, ECHO_PIN, unit="Fahrenheit").raw_distance()

    def test_raises_exception_no_pulse(self):
        """Test that SystemError raised if echo pulse not received."""
        # Typically, this error gets raised with a faulty cable.
        # Wrong echo pin simulates that condition
        wrong_echo_pin = ECHO_PIN - 1
        with self.assertRaises(SystemError):
            Measurement(TRIG_PIN, wrong_echo_pin).raw_distance()

    def test_depth(self):
        """Test the depth of a liquid"""
        value = self.metric_value
        raw_measurement = 48.80804985408
        hole_depth = 72
        metric_depth = value.depth(raw_measurement, hole_depth)
        self.assertAlmostEqual(metric_depth, 23.191950145920003)

        value2 = self.imperial_value
        hole_depth_inches = hole_depth * 0.394
        imperial_depth = value2.depth(raw_measurement, hole_depth_inches)
        self.assertAlmostEqual(imperial_depth, 9.137628357492481)

    def test_distance(self):
        """Test the distance measurement"""
        value = self.metric_value
        raw_measurement = 48.80804985408
        metric_distance = value.distance(raw_measurement)
        self.assertAlmostEqual(metric_distance, 48.80804985408)

        value2 = self.imperial_value
        imperial_distance = value2.distance(raw_measurement)
        self.assertAlmostEqual(imperial_distance, 19.23037164250752)

    def test_cylinder_volume_side(self):
        """Test the volume of liquid in a cylinder resting on its side."""
        value = self.metric_value
        depth = 20
        height = 120
        radius = 45
        cylinder_volume = value.cylinder_volume_side(depth, height, radius)
        self.assertAlmostEqual(cylinder_volume, 126.31926004538707)

        value2 = self.imperial_value
        depthi = 17
        heighti = 27
        radiusi = 18
        cylinder_volume_g = value2.cylinder_volume_side(depthi, heighti, radiusi)
        self.assertAlmostEqual(cylinder_volume_g, 55.28063419280857)

    def test_cylinder_volume_standing(self):
        """Test the volume of a liquid in a standing cylinder."""
        depth = 50
        radius = 30
        value = self.metric_value
        cylinder_volume = value.cylinder_volume_standing(depth, radius)
        self.assertAlmostEqual(cylinder_volume, 141.3716694115407)

        depthi = 24
        radiusi = 12
        value2 = self.imperial_value
        cylinder_volume_g = value2.cylinder_volume_standing(depthi, radiusi)
        self.assertAlmostEqual(cylinder_volume_g, 47.00149009007067)

    def test_cuboid_volume(self):
        """Test the volume of a liquid in a cuboid."""
        value = self.metric_value
        depth = 53
        width = 32
        length = 21
        cuboid_volume = value.cuboid_volume(depth, width, length)
        self.assertAlmostEqual(cuboid_volume, 35.616)

        value2 = self.imperial_value
        cuboid_volume_g = value2.cuboid_volume(depth, width, length)
        self.assertAlmostEqual(cuboid_volume_g, 154.1818181818182)

    def test_elliptical_cylinder_volume(self):
        """Test the volume of a liquid in an elliptical cylinder."""
        depth = 50
        semi_maj_axis = 24
        semi_min_axis = 15
        value = self.metric_value
        e_cyl_vol = value.elliptical_cylinder_volume(
            depth, semi_maj_axis, semi_min_axis
        )
        self.assertAlmostEqual(e_cyl_vol, 56.548667764616276)

        value2 = self.imperial_value
        e_cyl_vol_g = value2.elliptical_cylinder_volume(
            depth, semi_maj_axis, semi_min_axis
        )
        self.assertAlmostEqual(e_cyl_vol_g, 244.79942755245142)

    def test_elliptical_side_cylinder_volume(self):
        """Test the volume of a liquid in an elliptical cylinder on its side."""
        depth = 28
        height = 40
        width = 30
        length = 100
        value = self.metric_value
        e_cyl_vol_side = value.elliptical_side_cylinder_volume(
            depth, height, width, length
        )
        self.assertAlmostEqual(e_cyl_vol_side, 70.46757685376555)

        value2 = self.imperial_value
        e_cyl_vol_side_g = value2.elliptical_side_cylinder_volume(
            depth, height, width, length
        )
        self.assertAlmostEqual(e_cyl_vol_side_g, 305.05444525439634)

    def test_raise_cylinder_v_side(self):
        """Test ValueError raised with impossible depth values"""
        value = self.metric_value
        with self.assertRaises(ValueError):
            value.cylinder_volume_side(20, 80, 9)

        with self.assertRaises(ValueError):
            value.cylinder_volume_side(-1, 80, 20)

        with self.assertRaises(ValueError):
            value.elliptical_side_cylinder_volume(20, 15, 9, 120)

        with self.assertRaises(ValueError):
            value.elliptical_side_cylinder_volume(-1, 80, 20, 120)
