import hcsr04sensor.sensor as sensor


def main():
    '''Example script using hcsr04sensor module for Raspberry Pi'''
    trig_pin = 17
    echo_pin = 27
    unit = 'imperial'  # choices (metric or imperial)
    temperature = 68  # Fahrenheit
    round_to = 1

    #  Create a distance reading with the hcsr04 sensor module
    value = sensor.Measurement(trig_pin, echo_pin, temperature, unit)
    raw_measurement = value.raw_distance()

    # Calculate the distance in inches
    print "The Distance = {} inches".format(
        sensor.distance_imperial(raw_measurement, round_to)
        )

if __name__ == "__main__":
    main()
