###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
cuboid_volume= a * b * c
cuboid_area= 2*a*b + 2*a*c + 2*b*c 
print(f"The cuboid valume is {cuboid_volume} and the cuboid area is {cuboid_area}")