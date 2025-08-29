#bank_account.py

import threading

#defines the accounts functions
class bankAccount:
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.balance = initial_balance
        self._lock = threading.Lock()

    def deposit(self, amount: float):
        with self._lock:
            self.balance += amount

    def withdraw(self, amount: float) -> bool:
        with self._lock:
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False

    def get_balance(self) -> float:
        with self._lock:
            return self.balance

#deadlock prevention
def transfer(self, target_account, amount: float) -> bool:
    first, second = (self, target_account) if self.account_number < target_account.account_number else (target_account, self)
    with first._lock:
        with second._lock:
            if self.balance >= amount:
                self.balance -= amount
                target_account.balance += amount
                return True
            return False