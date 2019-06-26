"""Calculate the liquid volume of a cylinder"""
from hcsr04sensor import sensor

trig_pin = 17
echo_pin = 27
# default values
# temperature = 20 celcius
# unit = "metric"
# gpio_mode = GPIO.BCM

print(
    "Variances are due to error margins on seperate metric and imperial sensor readings"
)
# Get litres in a cylinder
cyl_depth_metric = 60  # centimeters
cyl_radius_metric = 15  # centimeters
value = sensor.Measurement(trig_pin, echo_pin)
distance = value.raw_distance()
water_depth_metric = value.depth(distance, cyl_depth_metric)
volume_litres = value.cylinder_volume_standing(water_depth_metric, cyl_radius_metric)
print("The liquid volume of the cylinder is {} litres".format(round(volume_litres, 1)))


# Get gallons in a cylinder
cyl_depth_imperial = cyl_depth_metric / 2.54  # inches
cyl_radius_imperial = cyl_radius_metric / 2.54  # inches
value = sensor.Measurement(trig_pin, echo_pin, temperature=68, unit="imperial")
distance = value.raw_distance()
water_depth_imperial = value.depth(distance, cyl_depth_imperial)
volume_gallons = value.cylinder_volume_standing(
    water_depth_imperial, cyl_radius_imperial
)
print(
    "The liquid volume of the cylinder is {} gallons".format(round(volume_gallons, 1))
)

