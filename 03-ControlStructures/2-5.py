###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >=1 and month <4:
    quarter = 1
elif month >=4 and month<7:
    quarter = 2
elif month >=7 and month <10:
    quarter = 3
    

print(f'Month {month} is in quarter {quarter}')