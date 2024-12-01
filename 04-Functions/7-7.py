def binary_number (number):
    check = True
    while len(number)>0:
        if number[0]== '1' or number[0]== '0':
            number = number[1:]
        else:
            check = False 
            break 
    return check 
def main():
   number = "1000103"
   print(binary_number(number))
   tekst="zegar"
   print(binary_number(tekst))
if __name__ == "__main__":
    main()