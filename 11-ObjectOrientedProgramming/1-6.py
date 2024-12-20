class Phone:
    def __init__(self, battery_level, connection_status, screen_status):
        self.battery_level = battery_level  # Battery percentage (0-100)
        self.connection_status = connection_status  # 'Connected' or 'Disconnected'
        self.screen_status = screen_status  # 'On' or 'Off'

    def charge_battery(self, charge_amount):
        """Charges the phone by a certain percentage."""
        self.battery_level += charge_amount
        if self.battery_level > 100:
            self.battery_level = 100  # Maximum battery is 100%
        print(f'Battery charged to {self.battery_level}%')

    def toggle_screen(self):
        """Toggles the screen on/off."""
        if self.screen_status == 'Off':
            self.screen_status = 'On'
        else:
            self.screen_status = 'Off'
        print(f'Screen is now {self.screen_status}')

    def connect_to_network(self):
        """Connects the phone to a network."""
        self.connection_status = 'Connected'
        print('Phone is now connected to the network.')

# Create a phone object with initial states
my_phone = Phone(battery_level=50, connection_status='Disconnected', screen_status='Off')

# Call methods to perform behaviors
my_phone.charge_battery(30)  # Charge the battery by 30%
my_phone.toggle_screen()  # Turn the screen on
my_phone.connect_to_network()  # Connect to network

# Display the current properties of the phone
print(f'Battery Level: {my_phone.battery_level}%')
print(f'Connection Status: {my_phone.connection_status}')
print(f'Screen Status: {my_phone.screen_status}')
