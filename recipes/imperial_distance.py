from hcsr04sensor import sensor

# Created by Al Audet
# MIT License


def main():
    """Calculate the distance of an object in inches using a HCSR04 sensor
       and a Raspberry Pi"""

    trig_pin = 17
    echo_pin = 27

    # Default values
    # unit = 'metric'
    # temperature = 20

    # Create a distance reading with the hcsr04 sensor module
    # and overide the default values for temp and unit)
    value = sensor.Measurement(trig_pin, echo_pin, temperature=68, unit="imperial")

    raw_measurement = value.raw_distance()

    # Calculate the distance in inches
    imperial_distance = value.distance(raw_measurement)
    print("The Distance = {} inches".format(round(imperial_distance, 1)))


if __name__ == "__main__":
    main()
