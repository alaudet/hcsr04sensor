from hcsr04sensor import sensor


def main():
    '''Example script using hcsr04sensor module for Raspberry Pi'''
    trig_pin = 17
    echo_pin = 27

    # Default values
    # unit = 'metric'
    # temperature = 20
    # round_to = 1

    hole_depth = 80  # centimeters

    # Create a distance reading with the hcsr04 sensor module

    value = sensor.Measurement(trig_pin,
                               echo_pin
                               )

    raw_measurement = value.raw_distance()

    # To overide default values you can pass the following to value
    # value = sensor.Measurement(trig_pin,
    #                            echo_pin,
    #                            temperature=10,
    #                            round_to=2
    #                            )

    # Calculate the liquid depth, in centimeters, of a hole filled
    # with liquid
    liquid_depth = value.depth_metric(raw_measurement, hole_depth)
    print("Depth = {} centimeters".format(liquid_depth))

if __name__ == "__main__":
    main()
