###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input('Letter from keyboard:')

str_number= '20303'
int_number= int(str_number)
print(int_number)

number = 10
bin_number = bin(number)
hex_number= hex(number)
print(f'Binary number is {bin_number}')
print(f'Hexadecimal number is {hex_number}')

sign = input('Enter the  unicode sign:')
integer= ord(sign)
print(f'Integer is {integer}')

negative_number = -17
absolute_value = abs(negative_number)
print(f'Absolute value is {absolute_value}')