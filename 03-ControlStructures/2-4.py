###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input('Enter number:'))
number2 = int(input('Enter number:'))
operator = input('Enter operator "+" , "-" , "*" or "/":')

if operator == '+':
    result = number1 + number2 
elif operator == '-':
    result = number1 - number2
elif operator == '*' :
    result = number1 * number2
elif operator == '/' :
    result = number1/number2
else :
    print("Incorrect operator")



# print result
print(f'{number1} {operator} {number2} = {result}')