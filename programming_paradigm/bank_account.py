

# #### Exercise 1: Creating a Student Class
# # Instructions:

# # Define a Student class with attributes like name and age. Include a method to display student information.

# class Student_class():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def student_info(self):
#             print (f"My name is {self.name}, and I am {self.age} years old.")


# StudentA = Student_class("Koba", 17)
# StudentA.student_info()



# #### Exercise 2: Creating a Product Catalog

# # Instruction:

# # Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock.

# class Products():
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def get_total_value(self):
#         total = self.quantity * self.price
#         print(f"The total value of {self.name} is {total}")
    

# item1 = Products("Crocodiles", 71, 2300)
# item1.get_total_value()






# Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. 
# Use command line arguments to interact with instances of this class.

# Task Description:
# You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, 
# which interfaces with the class through command line arguments to perform banking operations.

# bank_account.py:#

# Class Definition:
# Define a class named BankAccount.
# Use the __init__ method to initialize an account_balance attribute. 
# Optionally, accept an initial balance parameter, defaulting to zero.

class BankAccount():
    def __init__(self, account_balance, amount, initial_balance = 0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance
        self.amount = amount

    def deposit(self):
        print(f"{self.amount} + {self.account_balance}")

    def withdraw(self):
        if self.account_balance > self.amount:
            print(f"{self.amount} - {self.account_balance}")
        else:
            print(f"{self.account_balance}")
    def display_balance(self):
        print(f"Your account balance is ${self.account_balance}")




# Encapsulation and Behaviors:
# Implement deposit(amount), withdraw(amount), and display_balance() methods.
# deposit should add the specified amount to account_balance.
# withdraw should deduct the amount from account_balance if funds are sufficient, 
# returning True; otherwise, return False and do not alter the balance.
# display_balance should print the current balance in a user-friendly format.








# main-0.py for Command Line Interaction:
# This script utilizes BankAccount through command line arguments for banking operations.

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(amount=100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()