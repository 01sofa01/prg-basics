import random
dice_roll = random.randint(1,7)
special_number = dice_roll == 1 or dice_roll ==6
print(dice_roll)
print(f'Special number:{special_number}')