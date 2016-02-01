import hcsr04sensor.sensor as sensor


def main():
    '''Example script using hcsr04sensor module for Raspberry Pi'''
    trig_pin = 17
    echo_pin = 27

    #  Create a distance reading with the hcsr04 sensor module
    value = sensor.Measurement(trig_pin, echo_pin)

    # The default sample_size is 11 and sample_wait is 0.1
    # Increase speed by lowering the sample_size and sample_wait
    # The effect of reducing sample_size is larger variance in readings
    # The effect of lowering sample_wait is higher cpu usage and sensor
    # instability if you push it with too fast of a value.
    # These two options have been added to allow you to tweak a 
    # more optimal setting for your application.

    # e.g.
    raw_measurement = value.raw_distance(sample_size=5, sample_wait=0.03)

    # Calculate the distance in centimeters
    metric_distance = value.distance_metric(raw_measurement)
    print("The Distance = {} centimeters".format(metric_distance))

if __name__ == "__main__":
    main()
