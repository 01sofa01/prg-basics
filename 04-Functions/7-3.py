def month(x):
    if x == 1:
        return 'January'
    elif x == 2:
        return 'February'
    elif x == 3:
        return 'March'
    elif x == 4:
        return 'April'
    elif x == 5:
        return 'May'
    elif x == 6:
        return 'June'
    elif x == 7:
        return 'July'
    elif x == 8:
        return 'August'
    elif x == 9:
        return 'September'
    elif x == 10:
        return 'October'
    elif x == 11:
        return 'November'
    elif x == 12:
        return 'December'
    else:
        return 'Invalid month'

def main():
    try:
        entered_month = int(input('Enter the number of the month: '))  # Convert input to an integer
        counted_month = month(entered_month)  # Get the month name
        print(f'The name of the month {entered_month} is {counted_month}.')
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
