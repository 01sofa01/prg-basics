def ms_to_kmh(x):
    result = x/3.6
    return result 
speed = float(input('Enter your speed in ms:'))
result = ms_to_kmh(speed)
print(f'The speed {speed} ms is {result} kmh')


