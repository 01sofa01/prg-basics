###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
import math

def triangle_area(a,b,c):
    p = (a+b+c)/2
    result = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return result
side1 = 7
side2 = 24
side3 = 25
print(f'The area of ​​a triangle with sides {side1}, {side2} and {side3} is {triangle_area(side1, side2, side3)}')
