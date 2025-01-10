speed = float(input('Enter your speed in ms:'))

ms_to_kmh = lambda x : x*3.6

result = ms_to_kmh(speed)
print(f'The speed {speed} ms is {result} kmh')

