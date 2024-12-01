def credit_card (number): 
    hide_number = number[:2] 
    for i in range (9):
        hide_number += '*'
    hide_number += number[-4:]
    return hide_number
def main():
    number = '5290312400019022'
    print(credit_card(number))
if __name__ == "__main__":
    main()