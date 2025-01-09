###
# Creates a shopping list based on product names
# entered from the keyboard.
#

# shopping list file name
shopping_list = '08-FileHandling/shopping_list.txt'

# adds product name at the end of a shopping list
def add_product(file_name, num, product_name = "brak danych"):
   with open(file_name,'a') as file:
      file.write(str(num))
      file.write(". ")
      file.write(product_name)
      file.write('\n')
# Takes next product name from the keyboard
product = ""
n = 0
while product != "0":
   n += 1
   product = input('Enter product name (0 stops): ')
   if product != '0':
    add_product(shopping_list, n, product) # stops entering food names ('while' breaks)