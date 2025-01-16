import random as rn 

class Thermometer():
    def __init__(self):
        self.temp = round(rn.uniform(34,42),1)

        self.mode = False
    def turn_off_on(self):
        self.mode = not self.mode
    def measure(self):
        if self.mode == False:
            self.temp = round(rn.uniform(34,42),1)
            print(f"\nTemperature: {self.temp}", end=" ")
            if self.temp >= 41:
                print("CRITICAL TEMPERATURE!!")
            elif self.temp >= 37:
                print('Fever')
        else:
            print('Turned off')
