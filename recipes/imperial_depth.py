from hcsr04sensor import sensor

# Created by Al Audet
# MIT License


def main():
    """Calculate the depth of a liquid in inches using a HCSR04 sensor
       and a Raspberry Pi"""

    trig_pin = 17
    echo_pin = 27
    hole_depth = 31.5  # inches

    # Default values
    # unit = 'metric'
    # temperature = 20

    # Create a distance reading with the hcsr04 sensor module
    # and overide the default values for temp and unit)
    value = sensor.Measurement(trig_pin, echo_pin, temperature=68, unit="imperial")
    raw_measurement = value.raw_distance()

    # Calculate the liquid depth, in inches, of a hole filled
    # with liquid
    liquid_depth = value.depth(raw_measurement, hole_depth)
    print("Depth = {} inches".format(round(liquid_depth, 1)))


if __name__ == "__main__":
    main()
