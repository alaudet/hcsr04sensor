import hcsr04sensor.sensor as sensor


def main():
    '''Example script using hcsr04sensor module for Raspberry Pi'''
    trig_pin = 17
    echo_pin = 27
    unit = 'metric'  # choices (metric or imperial)
    temperature = 20  # Celcius for metric, Fahrenheit for imperial
    round_to = 1  # report a cleaner rounded output.

    #  Create a distance reading with the hcsr04 sensor module
    value = sensor.Measurement(trig_pin, echo_pin, temperature, unit, round_to)
    raw_measurement = value.raw_distance()

    # Calculate the distance in centimeters
    metric_distance = value.distance_metric(raw_measurement)
    print "The Distance = {} centimeters".format(metric_distance)

if __name__ == "__main__":
    main()
