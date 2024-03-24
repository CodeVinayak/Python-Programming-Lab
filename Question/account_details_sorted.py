class BankAccount:
    def __init__(self, accountholder_name, account_number, balance):
        self.accountholder_name = accountholder_name
        self.account_number = account_number
        self._balance = balance  # Using a single leading underscore to indicate it's a protected attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount < -2000:
            raise ValueError("Withdrawal amount exceeds the allowed limit.")
        self._balance -= amount

    def get_balance(self):
        return self._balance

class LoanAccount(BankAccount):
    def __init__(self, accountholder_name, account_number, balance, loan_amount):
        super().__init__(accountholder_name, account_number, balance)
        self.loan_amount = loan_amount

# Create instances and perform transactions
account1 = BankAccount("John Doe", "123456", 5000)
account1.deposit(2000)
account1.withdraw(1000)

loan_account = LoanAccount("Jane Smith", "654321", 10000, 5000)
loan_account.deposit(3000)
loan_account.withdraw(2000)

# Save account details to a file
with open("account_details.txt", "w") as file:
    # Write input data
    file.write("Accountholder Name, Account Number, Balance, Loan Amount\n")
    file.write(f"{account1.accountholder_name}, {account1.account_number}, {account1.get_balance()}, N/A\n")
    file.write(f"{loan_account.accountholder_name}, {loan_account.account_number}, {loan_account.get_balance()}, {loan_account.loan_amount}\n")

# Read the file and sort contents by balance
with open("account_details.txt", "r") as file:
    lines = file.readlines()
    lines.pop(0)  # Remove the header line
    sorted_lines = sorted(lines, key=lambda line: int(line.split(",")[2].strip()))

# Write sorted contents back to the file
with open("account_details_sorted.txt", "w") as file:
    file.write("Accountholder Name, Account Number, Balance, Loan Amount\n")
    file.writelines(sorted_lines)

# Display final balances
print(f"Final balance for {account1.accountholder_name}: {account1.get_balance()}")
print(f"Final balance for {loan_account.accountholder_name}: {loan_account.get_balance()}")
