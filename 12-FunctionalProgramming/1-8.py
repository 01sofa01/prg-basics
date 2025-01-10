name = str(input('Enter your name:'))
surname = str(input('Enter your surname:'))

initials = lambda name,surname : name[0].upper() + surname[0].upper()

result = initials(name, surname)
print(f'The initials of your name {name} and surname {surname} are {result}:')