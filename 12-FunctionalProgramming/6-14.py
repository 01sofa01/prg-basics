# Bottle filling data
fillings = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

# Constants
bottle_capacity = 500
tolerance_percentage = 2
tolerance = bottle_capacity * (tolerance_percentage / 100)

# Higher-order function for tolerance check
def is_incorrectly_filled(capacity, tolerance):
    return lambda fill: not (capacity - tolerance <= fill <= capacity + tolerance)

# Filter incorrectly filled bottles
incorrect_bottles = list(filter(is_incorrectly_filled(bottle_capacity, tolerance), fillings))

# Calculate the percentage of incorrectly filled bottles
incorrect_percentage = (len(incorrect_bottles) / len(fillings)) * 100

# Display the results
print(f"Bottle capacity:    {bottle_capacity}ml")
print(f"Filling tolerance:  {tolerance_percentage}%")
print(f"Filled bottles:     {','.join(map(str, fillings))}")
print(f"Incorrectly filled: {incorrect_percentage:.0f}%")
