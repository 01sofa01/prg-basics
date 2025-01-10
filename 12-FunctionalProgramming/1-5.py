def avg_speed(x,y,z):
    total_time = y + z/60
    result = x/(total_time)
    return result
    
    
distance = float(input('Enter your distance in km:'))
hours = float(input('Enter the amount of hours:'))
minutes = float(input('Enter the amount of minutes:'))

result = avg_speed(distance, hours, minutes)
print(f'The average speed with the distance {distance}, hours {hours} and minutes {minutes} is {result}')
