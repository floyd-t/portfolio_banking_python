#transaction.py

import threading

import random

from log.logger import log

from bank_account import bankAccount

class transactionSimulator:
    def __init__(self, account: bankAccount, num_users: int = 5, num_transactions: int = 10):
        self.account = account
        self.num_users = num_users
        self.num_transactions = num_transactions

    def _user_transactions(self, user_id: int):
        for _ in range(self.num_transactions):
            action = random.choice(["deposit", "withdraw"])
            amount = random.randint(1, 100)

            if action == "deposit":
                self.account.deposit(amount)
                log(f"User {user_id} deposited {amount}")
            else:
                success = self.account.withdraw(amount)
                if success:
                    log(f"User {user_id} withdrew {amount}")
                else:
                    log(f"User {user_id} failed to withdraw {amount} (insufficient funds)")

    def run(self):
        threads = []
        for user_id in range(self.num_users):
            t = threading.Thread(target=self._user_transactions, args=(user_id,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
