import hcsr04sensor.sensor as sensor


def main():
    '''Example script using hcsr04sensor module for Raspberry Pi'''
    trig_pin = 17
    echo_pin = 27
    # Default values
    # unit = 'metric'
    # temperature = 20
    # round_to = 1

    #  Create a distance reading with the hcsr04 sensor module
    value = sensor.Measurement(trig_pin, echo_pin)

    # The default sample_size is 11 and sample_wait is 0.1
    # Increase speed by lowering the sample_size and sample_wait
    # The effect of reducing sample is larger variance in readings
    # The effect of lowering sample_wait is high cpu usage and less
    # stability if you push it with too low a value.
    # The options have been added to allow you to tweak for a good balance 
    # for your application.

    # e.g.
    raw_measurement = value.raw_distance(sample_size=5, sample_wait=0.03)

    # To overide default values you can pass the following to value
    # value = sensor.Measurement(trig_pin,
    #                            echo_pin,
    #                            temperature=10,
    #                            round_to=2
    #                            )


    # Calculate the distance in centimeters
    metric_distance = value.distance_metric(raw_measurement)
    print("The Distance = {} centimeters".format(metric_distance))

if __name__ == "__main__":
    main()
