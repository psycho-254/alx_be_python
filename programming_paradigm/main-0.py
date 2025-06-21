# main-0.py

from bank_account import BankAccount

if __name__ == "__main__":
    account = BankAccount(100)
    account.display_balance()
    account.deposit(50)
    account.display_balance()
    if account.withdraw(30):
        print("Withdrawal successful.")
    else:
        print("Withdrawal failed.")
    account.display_balance()
    if not account.withdraw(200):
        print("Insufficient funds for withdrawal.")
    account.display_balance()
