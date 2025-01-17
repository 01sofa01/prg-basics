###
# The weather station report
#
temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# number of mesaurements
mesaurements = len(temperatures)

# calculates average temperature
temp_total = 0
for temp in temperatures:
   temp_total = sum(temperatures)
avg_temp = temp_total / mesaurements

# calculates min and max temperatures
min_temp = min(temperatures)
max_temp = max(temperatures)

# calculates number of days with negative temp
negative_temp = 0
i = 0
while i < mesaurements:
   if temperatures[i] < 0:
      negative_temp += 1
   i += 1

# prints out month report
print('Average temperature in March is:', avg_temp)
print('Min temp in March is', min_temp)
print('Max temp in March is:', max_temp)
print('Number of negative temp in March:', negative_temp)