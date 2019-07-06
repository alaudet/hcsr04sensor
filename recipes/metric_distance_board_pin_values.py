import RPi.GPIO as GPIO
from hcsr04sensor import sensor

# Created by Al Audet
# MIT License


def main():
    """Calculate the distance of an object in centimeters using a HCSR04 sensor
       and a Raspberry Pi"""
    # Use GPIO.BOARD values instead of BCM
    trig_pin = 11
    echo_pin = 13
    gpio_mode = GPIO.BOARD  # library uses GPIO.BCM by default
    # Default values
    # unit = 'metric'
    # temperature = 20

    # Create a distance reading with the hcsr04 sensor module
    # using GPIO.BOARD pin values.
    value = sensor.Measurement(trig_pin, echo_pin, gpio_mode=gpio_mode)
    raw_measurement = value.raw_distance()

    # Calculate the distance in centimeters
    print("The Distance = {} centimeters".format(round(raw_measurement, 1)))


if __name__ == "__main__":
    main()
