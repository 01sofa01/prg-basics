import math
height= float(input("Enter your height:"))
distance= 3.57 * math.sqrt(height)
print("The distance to the horizon is:", round(distance, 1))
print(f"The distance to the horizon is: {distance: .1f}")