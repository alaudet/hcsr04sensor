import hcsr04sensor.sensor as sensor


def main():
    '''Example script using hcsr04sensor module for Raspberry Pi'''
    trig_pin = 17
    echo_pin = 27
    unit = 'imperial'  # choices (metric or imperial)
    temperature = 68  # Fahrenheit
    round_to = 1
    hole_depth = 31.5  # inches

    #  Create a distance reading with the hcsr04 sensor module
    value = sensor.Measurement(trig_pin, echo_pin, temperature, unit, round_to)
    raw_measurement = value.raw_distance()

    # Calculate the liquid depth, in inches, of a hole filled
    # with liquid
    liquid_depth = value.depth_imperial(raw_measurement, hole_depth)    
    print "Depth = {} inches".format(liquid_depth)

if __name__ == "__main__":
    main()
