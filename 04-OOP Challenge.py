"""
Object Oriented Programming Challenge
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""
class Account:
    
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        
        self.balance += amount
        print("Your balance now is:")
        return self.balance
    
    
    def withdraw(self, amount):
        
        if amount > self.balance:
            print("Not sufficient funds :-/")
        else:
            self.balance -= amount
        
            print("Your balance now is:")
            return self.balance
        
    #Check info/balance of the account
    def __str__(self):
        
        return f"owner:{self.owner} \nCurrent balance:{self.balance}"
        
        
 """
 You can test it using for example:
 acct1 = Account("Alexander", 333333)
 
 This should give you the info of the account:
 print(acct1)
 
 For deposits:
 acct1.deposit(1000) 
 
 For withdraws:
 acct1.withdraw(777)
            
 """
