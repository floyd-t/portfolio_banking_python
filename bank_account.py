#bank_account.py

import threading

#defines the accounts functions
class bankAccount:
    #defines the way the number and balance should be (ensuring that the initial balance is 0 etc.)
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.balance = initial_balance
        self._lock = threading.Lock()

    #deposit allows money to increase through the += operator
    def deposit(self, amount: float):
        with self._lock:
            self.balance += amount

    #similar to deposit, but -= subtracts
    #if the balance is greater than the amount it wants remove it will do nothing
    def withdraw(self, amount: float) -> bool:
        with self._lock:
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False

    #this gets the final balance and reports it back to the caller (main.py, line 19)
    def get_balance(self) -> float:
        with self._lock:
            return self.balance

#deadlock prevention, it transfers the money and verifies it with a true or false (bool)
def transfer(self, target_account, amount: float) -> bool:
    #chooses which account has priority by choosing the account with the smaller number first
    first, second = (self, target_account) if self.account_number < target_account.account_number else (target_account, self)
    #checks that the account has enough funds, and only removes if true
    with first:
        with second:
            if self.balance >= amount:
                self.balance -= amount
                target_account.balance += amount
                return True
            return False
