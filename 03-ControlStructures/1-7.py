###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
is_bonus = True # does the employee receive a bonus
bonus = 0.15 # 15%

if is_bonus == True:
    total_salary = basic_salary + basic_salary *bonus 
else:
    print(basic_salary)

print(f'Basic salary: {basic_salary}')
print('Basic salary: ', basic_salary, 'dalszy tekst')
print(f'Bonus included? {bonus}')
print(f'Total salary: {total_salary}')