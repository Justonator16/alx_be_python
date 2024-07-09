# This is where l will perform unit tests for the main-0.py file 
import unittest
from bank_account import BankAccount

class TestBank(unittest.TestCase):
    amount = BankAccount(100)
    def test_deposit(self,amount):
        deposit = int(input("Enter deposit amount: "))
        self.assertEqual(deposit > 0,True)
    
    def test_withdraw(self,amount):
        withdrawal = int(input("Enter withdrawal amount: "))
        self.assertEqual(amount.withdraw(withdrawal),True)

if __name__ == "__main__":
  unittest.main()

    