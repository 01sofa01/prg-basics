speed = [48,47,54,50,42,68,39,46]

speed_too_high = list(filter(lambda x: x>50, speed))
print(speed_too_high)