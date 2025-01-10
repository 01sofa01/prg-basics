distance = float(input('Enter your distance in km:'))
hours = float(input('Enter the amount of hours:'))
minutes = float(input('Enter the amount of minutes:'))
total_time = hours + minutes/60
avg_speed = lambda distance, total_time : distance/total_time
result = avg_speed(distance, total_time)
print(f'Your average speed is {result}')