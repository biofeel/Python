class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"{self.name} {self.account_balance}")
        return self
    def transfer_money(self, name, amount):
        self.account_balance -= amount
        name.account_balance += amount

michael = User("Michael", "email@gmail.com")
ronald = User("Ronald", "email@goooogle.com")
chris = User("Chris", "email@yahoo.com")
print(michael.email)
michael.make_deposit(100)
michael.make_deposit(200)
michael.make_deposit(300)
ronald.make_deposit(200)
ronald.make_deposit(100)
chris.make_deposit(300)
michael.make_withdrawal(25)
ronald.make_withdrawal(25)
ronald.make_withdrawal(125)
chris.make_withdrawal(25)
chris.make_withdrawal(55)
chris.make_withdrawal(45)
print(michael.account_balance)
print(ronald.account_balance)
print(chris.account_balance)
michael.display_user_balance()
ronald.display_user_balance()
chris.display_user_balance()

michael.transfer_money(chris, 75)
print(chris.account_balance)
print(michael.account_balance)
print(ronald.account_balance)