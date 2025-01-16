def f(flights):
    # Calculate the average number of passengers
    avg_passengers = sum(flights.values()) / len(flights)
    # Count flights with passengers greater than the average
    return sum(1 for passengers in flights.values() if passengers > avg_passengers)

# Example usage
print(f({"LO231": 150, "BA787": 120, "NZ15": 30}))  # Output: 2
print(f({"LO231": 150, "BA787": 20, "NZ15": 30}))   # Output: 1
