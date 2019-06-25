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
    # Default values
    # unit = 'metric'
    # temperature = 20
    # round_to = 1

    # Create a distance reading with the hcsr04 sensor module
    # using GPIO.BOARD pin values.
    value = sensor.Measurement(trig_pin, echo_pin, gpio_mode=GPIO.BOARD)
    raw_measurement = value.raw_distance()

    # Calculate the distance in centimeters
    metric_distance = value.distance(raw_measurement)
    print("The Distance = {} centimeters".format(metric_distance))


if __name__ == "__main__":
    main()
