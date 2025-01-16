

import matplotlib.pyplot as plt

# Temperature data
weather_in_cities = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Create arrays for cities (x-axis) and temperatures (y-axis) using map()
cities = list(weather_in_cities.keys())
temperatures = list(weather_in_cities.values())

# Create the bar chart
plt.bar(cities, temperatures, color='skyblue')

# Add chart title and axis labels
plt.title("Temperatures Recorded in Cities", fontsize=14)
plt.xlabel("Cities", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)

# Show gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
plt.tight_layout()  # Adjust layout for better spacing
plt.show()
