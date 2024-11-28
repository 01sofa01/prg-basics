###
# A program that prints your height both in cm and in feet and inches.
#
cm = 180
feet = int(cm/30.48)
inches = cm/2.54%12
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet}feet and {inches: .1f}inches')