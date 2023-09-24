class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print("deposit(). New balance: {}".format(self._account_balance))
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print("Withdraw(). New balance: {}".format(self._account_balance))
        else:
            print("Invalid withdrawal amount")

    def display_balance(self):
        print("Account balance for (Account {}: {}): {}".format(
            self._account_holder_name, self._account_number, self._account_balance))

account = BankAccount(account_number="153378567", account_holder_name="pathiri", initial_balance=5000.0)

account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()