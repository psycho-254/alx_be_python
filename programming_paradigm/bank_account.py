# Task Description:
# You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, 
# which interfaces with the class through command line arguments to perform banking operations.

# bank_account.py:
# Class Definition:

# Define a class named BankAccount.
# Use the __init__ method to initialize an account_balance attribute. 
# Optionally, accept an initial balance parameter, defaulting to zero.
# Encapsulation and Behaviors:

# Implement deposit(amount), withdraw(amount), and display_balance() methods.
# deposit should add the specified amount to account_balance.
# withdraw should deduct the amount from account_balance if funds are sufficient, 
# returning True; otherwise, return False and do not alter the balance.
# display_balance should print the current balance in a user-friendly format.

# bank_account.py

# bank_account.py

class BankAccount:

   def __init__(self, account_balance=0):
      self.account_balance = account_balance
   
   def deposit(self, amount):
      self.account_balance += amount

   def withdraw(self, amount):
      if amount <= self.account_balance:
        self.account_balance -= amount
        return True
      else:
         return(False)
      
   def display_balance(self):
      print(f"Current Balanceee: ${self.account_balance:.2f}")




# Implementation Notes for you:
# Ensure your BankAccount class in bank_account.py correctly implements the specified functionalities and 
# adheres to the principles of encapsulation.
# Use main.py to test your BankAccount class by performing various operations. 
# Adjust the initial balance as needed for testing different scenarios.

# Example usage:
# if __name__ == "__main__":
#     account = BankAccount(100)
#     account.display_balance()  # Should print: Current balance: $100.00

