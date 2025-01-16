class BankAccount:
    def __init__(self, account_number):
        """Initialize the bank account with a number and a balance of 0."""
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount. Amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient funds exist."""
        if amount > self.balance:
            print("Insufficient funds on the account.")
        elif amount > 0:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount. Amount must be positive.")

    def display_info(self):
        """Display the account number and balance."""
        print(f"Bank Account No: {self.account_number}")
        print(f"Balance: PLN {self.balance:.2f}")

# Usage of the program
# Step 1: Create a bank account
account = BankAccount("12 3456 5555 9090 1111 0000 7722")

# Step 2: Display account balance
account.display_info()

# Step 3: Deposit PLN 25.30
account.deposit(25.30)

# Step 4: Display account balance
account.display_info()

# Step 5: Withdraw PLN 31.70
account.withdraw(31.70)

# Step 6: Display account balance
account.display_info()

# Step 7: Withdraw PLN 14
account.withdraw(14)

# Step 8: Display account balance
account.display_info()



        