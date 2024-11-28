###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results
radius = float(input('Enter the radius value:'))
PI_value = 3.14
area = PI_value*radius**2
circumference = 2*PI_value*radius
print(f'The area is {area:.2f} and the circumference is {circumference: .2f}')