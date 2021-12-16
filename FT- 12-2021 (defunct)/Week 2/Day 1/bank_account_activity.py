# In this activity, you are going to model a bank account.

#     Create a class called BankAccount.
#     Add properties for balance and account_number
#     Allow the user to deposit funds to the account. This can be accomplished by adding a deposit function to the BankAccount class.
#     Allow the user to withdraw funds from the account. This can be accomplished by adding a withdraw function to the BankAccount class.
#     Allow the user to transfer funds between two accounts. This can be accomplished by adding a transfer_funds function to the BankAccount class.
#     After creating the BankAccount class, along with all the functions make sure to create instance of BankAccount and perform actions.

# Example:

# checking_account = BankAccount("FD332", 100)
# checking_account.deposit(50) 
# print(checking_account.balance) # $150 

class BankAccount:
    def __init__(self, checking, savings):
        self.checking = checking
        self.savings = savings
        self.deposit_amount = ""
        self.transfer_ammount = ""
    
    def deposit(self):
        self.deposit_amount = int(input("How much would you like to deposit: "))
        self.savings += self.deposit_amount

    def withdraw(self):
        self.withdraw_amount = int(input("How much would you like to withdraw: "))
        self.checking -= self.withdraw_amount


bank_account = BankAccount(1000, 50000)
print("Before deposit")
print(bank_account. checking)
print(bank_account. savings)
print("\n")

print("After deposit")
bank_account.deposit()
print(bank_account. savings)


print("Before withdraw")
print(bank_account. checking)
print(bank_account. savings)
print("\n")

print("After withdraw")
bank_account.withdraw()
print(bank_account. checking)

#### here's how we would transfer funds
# see class notes, the important thing is you can pass objects as arguments in propoerties

