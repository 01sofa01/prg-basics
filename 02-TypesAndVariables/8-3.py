###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
temperature_celsius = float(input("Enter the temperature in Celsius:"))
temperature_kelvin = temperature_celsius + 273.15
temperature_farenheit = (9/5 * temperature_celsius) + 32
print(temperature_celsius)
print(temperature_kelvin)
print(temperature_farenheit)