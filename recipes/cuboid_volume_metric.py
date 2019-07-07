"""Calculate the liquid volume of a cylinder"""
from hcsr04sensor import sensor

trig_pin = 17
echo_pin = 27
cuboid_depth = 40  # distance from sensor to bottom of box
cuboid_length = 24
cuboid_width = 30

#
# Calculate the litres in a box like container
value = sensor.Measurement(trig_pin, echo_pin)
raw_distance = value.raw_distance()
liquid_depth = value.depth(raw_distance, cuboid_depth)
volume_litres = value.cuboid_volume(liquid_depth, cuboid_width, cuboid_length)
print("The liquid volume of the cuboid is {} litres".format(round(volume_litres, 1)))

