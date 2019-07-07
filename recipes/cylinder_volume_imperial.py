"""Calculate the liquid volume of a standing cylinder"""
from hcsr04sensor import sensor

trig_pin = 17
echo_pin = 27
temperature = 68  # Farenheit
unit = "imperial"
bottom_depth = 38  # inches from the sensor to the bottom of the cylinder
cyl_radius = 15  # diameter / 2

# Get gallons in a cylinder
value = sensor.Measurement(trig_pin, echo_pin, temperature, unit)
raw_measurement = value.raw_distance()  # distance to the liquid
liquid_depth = value.depth(raw_measurement, bottom_depth)  # inches

volume_gallons = value.cylinder_volume_standing(liquid_depth, cyl_radius)
print(
    "The liquid volume of the cylinder is {} gallons".format(round(volume_gallons, 1))
)
