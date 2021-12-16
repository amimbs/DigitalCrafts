# Unit Testing
# Test Driven Development - write your test before you even write code

# 1) write a failing test
# 2) Make the test pass by implemeting the code
# 3) Refactor - how can we make our tets better without changing its functionality
# 4) Repeat

# Unit test rules
# 1. Unit test should be indepenent
# 2. Unit test should NEVER wait for human input
# 3. Unit tests should be repeatable


# BankAccount
# 
# - deposit
# - withdraw
# - transfer


# the setUP function is executed before each other test

# tearDown is a function that gets fired after running --->
# each test - great function when you need to clean up the resources. Great if your test creates a file or changes things, teardown resets or deletes the remnants


import unittest 
from bank_account import BankAccount  

# BankAccountTests class inherits from the TestCase class
class BankAccountTests(unittest.TestCase): 

  # setUp is fired before each test
  def setUp(self): 
    print("SETUP")
    self.bank_account = BankAccount("1234", 100)

  # Your test function should begin with "test" word
  def test_deposit_into_bank_account(self):
    print("test_deposit_into_bank_account") 
    self.bank_account.deposit(50)
    self.assertEqual(150, self.bank_account.balance)

  def test_transfer_funds(self): 
    print("test_transfer_funds")
   
    to_account = BankAccount("4567", 50)

    self.bank_account.transfer(50, to_account)
    self.assertEqual(50, self.bank_account.balance)
    self.assertEqual(100, to_account.balance)

  # fired after each test
  def tearDown(self): 
    print("TEARDOWN")

# run the test
unittest.main()