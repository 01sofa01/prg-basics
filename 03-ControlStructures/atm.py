# ATM (cash machine) simulator

balance = 1000  # Initial balance
pin = '1111'  # Initial 4-digit PIN code

# PIN authentication
entered_pin = input("Enter your 4-digit PIN: ")
if entered_pin != pin:
    print("Invalid PIN. Access denied.")
else:
    while True:
        print()
        print("ATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check PIN")
        print("5. Change PIN")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        print()

        if choice == '1':  # Check balance
            print(f"Your current balance is: €{balance}")
        elif choice == '2':  # Deposit
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                else:
                    balance += amount
                    print(f"€{amount:.2f} has been deposited. New balance: €{balance:.2f}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '3':  # Withdraw
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                elif amount <= balance:
                    balance -= amount
                    print(f"€{amount:.2f} has been withdrawn. New balance: €{balance:.2f}")
                else:
                    print("Insufficient balance.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '4':  # Check PIN
            print(f"Your current PIN is: {pin}")
        elif choice == '5':  # Change PIN
            current_pin = input("Enter your current PIN: ")
            if current_pin == pin:
                new_pin = input("Enter a new 4-digit PIN: ")
                confirm_pin = input("Confirm the new PIN: ")
                if new_pin == confirm_pin and len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("Your PIN has been successfully changed.")
                else:
                    print("PIN change failed. Ensure your new PIN is 4 digits and matches the confirmation.")
            else:
                print("Incorrect current PIN.")
        elif choice == '6':  # Exit
            print("Exiting... Thank you for using the ATM!")
            break
        else:
            print("Invalid option. Please try again.")