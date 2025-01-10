number = int(input('Enter your number:'))

is_number_even = lambda number :  number % 2 == 0 
if is_number_even(number):
    print('The entered number is even.')
else :
    print('The entered number is odd.')