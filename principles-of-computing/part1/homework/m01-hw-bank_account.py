class BankAccount:
    """Class definition modeling the behavior of a simple bank account
    """

    def __init__(self, initial_balance):
        """Creates an account with the given balance.

        Args:
            initial_balance (int or float): initial bank account balance
        """
        self._balance = initial_balance
        self._fees = 0

    def deposit(self, amount):
        """Deposits the amount into the account.

        Args:
            amount (int or float): amount to deposit into the bank account
        """
        self._balance += amount

    def withdraw(self, amount):
        """Withdraw the amount from the account. Each withdrawal resulting
        in a negative balance also deducts a penalty fee of 5 dollars
        from the balance.

        Args:
            amount (int or float): amount to withdraw from the bank account
        """
        self._balance -= amount
        if self._balance < 0:
            self._fees += 5
            self._balance -= 5


    def get_balance(self):
        """Returns the current balance in the account."""
        return self._balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self._fees


# Test case 1: It should print the values 10 and 5, respectively, since the withdrawal incurs a fee of 5 dollars.
my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(20)
print("Test Case 1 Result ....")
print(my_account.get_balance(), my_account.get_fees())

# Test case 2
my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5)
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50)
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
print("Test Case 2 Result ...")
print(my_account.get_balance(), my_account.get_fees())