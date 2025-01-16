employee = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]
last_name = list(map(lambda x : x[0].upper() + " " + x[1], employee))
print('\n Last names in capital letters:')
for name in last_name:
    print(name)