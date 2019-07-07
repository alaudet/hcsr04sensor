from hcsr04sensor import sensor

# Created by Al Audet
# MIT License


def main():
    """Calculate the distance of an object in centimeters using a HCSR04 sensor
       and a Raspberry Pi. This script allows for a quicker reading by
       decreasing the number of samples and forcing the readings to be
       taken at quicker intervals."""

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
    print("The Distance = {} centimeters".format(round(raw_measurement, 1)))


if __name__ == "__main__":
    main()
