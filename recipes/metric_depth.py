from hcsr04sensor import sensor

# Created by Al Audet
# MIT License


def main():
    """Calculate the depth of a liquid in centimeters using a HCSR04 sensor
       and a Raspberry Pi"""

    trig_pin = 17
    echo_pin = 27

    # Default values
    # unit = 'metric'
    # temperature = 20

    hole_depth = 80  # centimeters

    # Create a distance reading with the hcsr04 sensor module

    value = sensor.Measurement(trig_pin, echo_pin)

    raw_measurement = value.raw_distance()

    # To overide default values you can pass the following to value
    # value = sensor.Measurement(trig_pin,
    #                            echo_pin,
    #                            temperature=10,
    #                            )

    # Calculate the liquid depth, in centimeters, of a hole filled
    # with liquid
    liquid_depth = value.depth(raw_measurement, hole_depth)
    print("Depth = {} centimeters".format(round(liquid_depth, 1)))


if __name__ == "__main__":
    main()
