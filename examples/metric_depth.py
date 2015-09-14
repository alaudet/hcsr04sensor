import hcsr04sensor.sensor as sensor


def main():
    '''Example script using hcsr04sensor module for Raspberry Pi'''
    trig_pin = 17
    echo_pin = 27
    unit = 'metric'  # choices (metric or imperial)
    temperature = 20  # Celcius for metric, Fahrenheit for imperial
    round_to = 1  # report a cleaner rounded output.
    hole_depth = 80  # centimeters

    # Create a distance reading with the hcsr04 sensor module
    value = sensor.Measurement(trig_pin, echo_pin, temperature, unit, round_to)
    raw_measurement = value.raw_distance()

    # Calculate the liquid depth, in centimeters, of a hole filled
    # with liquid
    liquid_depth = value.depth_metric(raw_measurement, hole_depth)
    print("Depth = {} centimeters".format(liquid_depth))

if __name__ == "__main__":
    main()
