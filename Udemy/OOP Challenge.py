'''
Object Oriented Programming Challenge

For this challenge, create a bank account class that has two attributes:

    owner
    balance

and two methods:

    deposit
    withdraw

As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to
make sure the account can't be overdrawn.

'''


class Account():

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        # you cannot use print() here, use return.
        return f'Account Owner: {self.name}\nAccount Balance: ${self.balance}'

    def deposit(self, dAmount):
        self.balance += dAmount
        print(f'Deposit Accepted, ${dAmount}')

    def withdraw(self, wAmount):
        if self.balance >= wAmount:
            self.balance -= wAmount
            print(f'Withdrawal Accpeted, {wAmount}')
        else:
            print('Not enough balance to withdraw!')


acct1 = Account('Gerard', 100) 
print(acct1)

acct1.deposit(150)
print(acct1)

acct1.withdraw(475)
print(acct1)
