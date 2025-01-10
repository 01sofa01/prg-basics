def ms_to_kmh(x):
    result = x/1000*3600
    return result 
speed = int(input('Enter your speed in ms:'))
result = ms_to_kmh(speed)
print(f'The speed {speed} ms is {result} kmh')