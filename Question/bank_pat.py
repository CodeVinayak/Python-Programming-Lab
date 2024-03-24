"""
Write a Python Program to create a BankAccount class with attributes accountholder name, account number, and balance. Implement methods deposit(amount) and withdraw(amount) to handle transactions. Create an instance of the class, perform a few transactions, and display the final balance.Throw an exception whenever the balance of an account holder drops beyond 
Rs.2000. Create a derived class loan account under the base class Bank Account Which will have all the features of the base class and attributes loan amount in the derived class. Use all the access specifiers in the above program.
Create a file that will hold the details of all the account holders and sort the file contents in ascending order of their balances. The file should contain both the input and the output data
"""

class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < -2000:
            raise ValueError("Withdrawal not allowed. Balance would drop below Rs.2000.")
        self.balance -= amount

    def display_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: Rs. {self.balance}\n")


class LoanAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance, loan_amount):
        super().__init__(account_holder, account_number, balance)
        self.loan_amount = loan_amount

    def display_details(self):
        super().display_details()
        print(f"Loan Amount: Rs. {self.loan_amount}\n")


# Example Usage
accounts = [
    BankAccount("Alice", "001", 5000),
    LoanAccount("Bob", "002", 3000, 20000),
    BankAccount("Charlie", "003", 7000),
    LoanAccount("David", "004", 1000, 15000),
]

# Perform transactions
for account in accounts:
    try:
        account.deposit(2000)
        account.withdraw(1000)
    except ValueError as ve:
        print(f"Error: {ve}")

# Display final balances
for account in accounts:
    account.display_details()

# Sort accounts by balance
sorted_accounts = sorted(accounts, key=lambda acc: acc.balance)

# Write details to file
file_path = "account_details.txt"
with open(file_path, "w") as file:
    for account in sorted_accounts:
        details = f"{account.display_details()}\n"
        file.write(details)

print(f"Operation completed. Check '{file_path}' for details.")
account_details_sorted.txt