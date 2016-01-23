import hcsr04sensor.sensor as sensor


def main():
    '''Example script using hcsr04sensor module for Raspberry Pi'''
    trig_pin = 17
    echo_pin = 27
    
    #Default units for unit, temperature and round_to
    #unit = 'metric' can be overidden with unit='imperial'
    #temperature = 20 can be overidden with temperature = 68
    #round_to = 1 can be overidden with round_to=x (where x is the decimal place)

    unit = 'imperial'  # choices (metric or imperial)
    # round_to = 2 

    #  Create a distance reading with the hcsr04 sensor module
    value = sensor.Measurement(trig_pin, 
                               echo_pin,
                               unit=unit,
                               temperature=68,
                               round_to=2
                               )
    
    value.print_them()
    raw_measurement = value.raw_distance(sample_size=11)
    value.print_them()
    # Calculate the distance in inches
    imperial_distance = value.distance_imperial(raw_measurement)
    print("The Distance = {} inches".format(imperial_distance))

if __name__ == "__main__":
    main()
