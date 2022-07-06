from typing import NamedTuple


class User:
    def __init__(self,name,email):
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
        print(self.account_balance)
        return self

guido = User("Guido van Rossum", "rawrxd@protonmail.com")
maxi = User('Maxi', 'macs@gmail.com')
richard = User('Rich', 'dick21@yahoo.com')

guido.make_deposit(20).make_deposit(67).make_deposit(103).make_withdrawal(56).display_user_balance()
maxi.make_deposit(1200).make_withdrawal(50).make_deposit(12).make_withdrawal(800).display_user_balance()
richard.make_deposit(565).make_withdrawal(80).make_withdrawal(10).make_withdrawal(3).display_user_balance()

