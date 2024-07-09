class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = account_balance

# deposit should add the specified amount to account_balance
    def deposit(self ,amount):
        self.account_balance += amount
# withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
    def withdraw(self, amount):
        deduction = self.account_balance - amount
        if  deduction < 0:
            return False
        else:
            return True

# display_balance should print the current balance in a user-friendly format.
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

