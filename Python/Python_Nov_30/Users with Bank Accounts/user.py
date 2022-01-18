class BankAccount:
    ninja_bonus = []
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.ninja_bonus.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        elif self.balance <= amount:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"{self.name} Account Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_ninja_bonus(cls):
        for acct in cls.ninja_bonus:
            acct.display_account_info()

# account1 = BankAccount(0.07, 0)
# account2 = BankAccount(0.05, 400)

# account1.deposit(100).deposit(50).deposit(300).withdraw(150).display_account_info()
# account2.deposit(240).deposit(100).withdraw(101).withdraw(60).display_account_info()

# BankAccount.print_ninja_bonus()

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(self.name, int_rate=.03, balance=0)
    def make_deposit(self):
        self.account.deposit()
        return self
    def make_withdrawal(self):
        self.account.withdraw()
        return self
    def display_user_balance(self):
        print(f"{self.name} - balance: {self.account}")
        return self
    def transfer_money(self, name, amount):
        self.account -= amount
        name.account += amount
        return self

michael = User("Michael")

michael.account.deposit(30)
michael.account.withdraw(20)
michael.account.display_account_info()