###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption:'))
total_fuel_consumption = distance/100*fuel_consumption
total_cost = total_fuel_consumption*fuel_price
print("Total fuel consumption is:", total_fuel_consumption)
print("Total fuel cost is:",total_cost)