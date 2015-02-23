import hcsr04sensor.sensor as sensor


def main():
    '''Example script using hcsr04sensor module for Raspberry Pi'''
    trig_pin = 17
    echo_pin = 27
    unit = 'celcius'  # may also enter 'imperial' here
    temperature = 68
    round_to = 1  # report a cleaner rounded output.
    hole_depth = 60  # centimeters
    hole_depth_in = hole_depth * 0.394

    if unit == 'imperial':
        print 'Reading at {} degrees Fahrenheit '.format(temperature)
        # HCSR04 sensor only understands metric. Convert to Celcius before
        # passing the temperature to the hcsr04sensor module.
        temperature = (temperature - 32) * 0.5556
    elif unit == 'celcius':
        print 'Reading at {} degrees Celcius '.format(temperature)
    else:
        print "Unit must be imperial or celcius"
        print "Please try again"
        exit(0)

    # Create a distance reading with the hcsr04 sensor module
    value = sensor.Measurement(trig_pin, echo_pin, temperature)
    raw_measurement = value.raw_distance()

    # This is the raw distance in centimeters
    print "The Unrounded Distance = {} centimeters".format(raw_measurement)

    # return metric Distance reading in centimeters
    print "The Distance = {} centimeters".format(
        sensor.distance_metric(raw_measurement, round_to)
        )

    # Return an imperial Distance reading in inches
    print "The Distance = {} inches".format(
        sensor.distance_imperial(raw_measurement, round_to)
        )

    # Return the metric liquid depth, in centimeters, of a hole filled
    # with liquid
    print "Depth = {} centimeters".format(
        sensor.depth_metric(raw_measurement, hole_depth, round_to)
        )

    # Return the imperial liquid depth, in inches, of a hole filled with liquid
    print "Depth = {} inches".format(
        sensor.depth_imperial(raw_measurement, hole_depth_in, round_to)
        )

if __name__ == "__main__":
    main()
