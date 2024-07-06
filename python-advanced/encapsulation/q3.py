class AccountError(Exception):
    pass 

class MyAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  # Private attribute
        self.__account_balance = initial_balance  # Private attribute

    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_balance(self):
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__account_balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__account_balance:
            raise ValueError("Insufficient balance")
        self.__account_balance -= amount

    # Optional deleter for balance, though not commonly needed
    @account_balance.deleter
    def balance(self):
        del self.__account_balance

    # Preventing direct access to account_number setter to enforce read-only behavior
    @account_number.setter
    def account_number(self, value):
        raise AccountError("Cannot change the account number")

# Example usage:
try:
    account1 = MyAccount("1234567890", 1000)
    print(f"Account number: {account1.account_number}")
    print(f"Balance: {account1.account_balance}")

    # Trying to change account number should raise an exception
    account1.account_number = "0987654321"

except AccountError as e:
    print(f"Error: {e}")

except ValueError as e:
    print(f"Error: {e}")
