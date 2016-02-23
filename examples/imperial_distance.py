from hcsr04sensor import sensor


def main():
    '''Example script using hcsr04sensor module for Raspberry Pi'''
    trig_pin = 17
    echo_pin = 27

    # Default values
    # unit = 'metric'
    # temperature = 20
    # round_to = 1

    # Create a distance reading with the hcsr04 sensor module
    # and overide the default values for temp, unit and rounding)
    value = sensor.Measurement(trig_pin,
                               echo_pin,
                               temperature=68,
                               unit='imperial',
                               round_to=2
                               )

    raw_measurement = value.raw_distance()

    # Calculate the distance in inches
    imperial_distance = value.distance_imperial(raw_measurement)
    print("The Distance = {} inches".format(imperial_distance))

if __name__ == "__main__":
    main()
