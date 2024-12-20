class TaxiRide:
    def __init__(self, rate_per_km):
        """Initializes the taxi ride with a rate per kilometer."""
        self.rate_per_km = rate_per_km  # Rate per kilometer (in €)
        self.distance = 0  # Distance of the ride (in km)
        self.fare = 0  # Fare to be calculated (in €)

    def calculate_fare(self, distance):
        """Calculates the fare based on the distance and rate per kilometer."""
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        """Prints the receipt containing distance, rate, and fare."""
        print("------- Taxi Ride Receipt -------")
        print(f"Distance: {self.distance} km")
        print(f"Rate: €{self.rate_per_km:.2f} per km")
        print(f"Fare: €{self.fare:.2f}")
        print("---------------------------------")
def main():
    # Create the first TaxiRide object with a rate of €2 per kilometer
    ride1 = TaxiRide(rate_per_km=2)
    # Calculate the fare for a ride of 10 kilometers
    ride1.calculate_fare(distance=10)
    # Print the receipt for the first ride
    ride1.print_receipt()

    # Create the second TaxiRide object with a rate of €3 per kilometer
    ride2 = TaxiRide(rate_per_km=3)
    # Calculate the fare for a ride of 15 kilometers
    ride2.calculate_fare(distance=15)
    # Print the receipt for the second ride
    ride2.print_receipt()

if __name__ == "__main__":
    main()

