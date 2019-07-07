"""Calculate the liquid volume of an elliptical standing cylinder"""
from hcsr04sensor import sensor

trig_pin = 17
echo_pin = 27
# default values
# temperature = 20 celcius
# unit = "metric"
# gpio_mode = GPIO.BCM

# Get litres in a cylinder
semi_maj_axis = 45  # centimeters radius of semi major axis
semi_min_axis = 30  # centimeters radius of semi minor axis
cyl_depth = 96  # cm from sensor to bottom
value = sensor.Measurement(trig_pin, echo_pin)
# for imperial add temp and unit and change all cm values to inches
# value = sensor.Measurement(trig_pin, echo_pin, 68, 'imperial')
distance = value.raw_distance()

water_depth_metric = value.depth(distance, cyl_depth)

volume_litres = value.elliptical_cylinder_volume(
    water_depth_metric, semi_maj_axis, semi_min_axis
)
print(
    "The liquid volume of the elliptical cylinder is {} litres".format(
        round(volume_litres, 1)
    )
)
