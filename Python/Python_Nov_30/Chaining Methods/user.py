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
        return self

michael = User("Michael", "email@gmail.com")
ronald = User("Ronald", "email@goooogle.com")
chris = User("Chris", "email@yahoo.com")

michael.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(25).transfer_money(chris, 75).display_user_balance()
ronald.make_deposit(200).make_deposit(100).make_withdrawal(25).make_withdrawal(125).display_user_balance()
chris.make_deposit(300).make_withdrawal(25).make_withdrawal(55).make_withdrawal(45).display_user_balance()
