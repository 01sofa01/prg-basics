# ###
# Writes Seven Wonders of the World to a file
#
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = '08-FileHandling/seven_wonders.txt'

# Sort data alphabetically
sorted = sorted(seven_wonders)

# Write data to the file
with open(file_name, 'w') as file:
    for item in sorted:
        file.write(item)
        file.write('\n')

x=2.0987654
print("x = {0}, a y = 3, jednak x = {0}".format(x))