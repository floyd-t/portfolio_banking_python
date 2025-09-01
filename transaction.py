#transaction.py

import threading
import random

#imports classes from other files
from logger import log
from bank_account import bankAccount


class transactionSimulator:
    #this sets the default value of users and transactions
    #this can be changed in main.py but operates as a backup
    def __init__(self, account: bankAccount, num_users: int = 5, num_transactions: int = 10):
        self.account = account
        self.num_users = num_users
        self.num_transactions = num_transactions

    #chooses whether to withdraw or deposit and picks a value between 1 and 100
    def _user_transactions(self, user_id: int):
        for _ in range(self.num_transactions):
            action = random.choice(["deposit", "withdraw"])
            amount = random.randint(1, 100)

            #logs deposits after being completed
            if action == "deposit":
                self.account.deposit(amount)
                log(f"User {user_id} deposited {amount}")
            #logs withdrawals
            #however if there are insufficient funds it will log a failure instead of completing the withdrawal
            else:
                success = self.account.withdraw(amount)
                if success:
                    log(f"User {user_id} withdrew {amount}")
                else:
                    log(f"User {user_id} failed to withdraw {amount} (insufficient funds)")

    #creates threads that allow the users to use the same account at the same time
    #it is able to do this due to how threads work and how they can operate in parallel with the main program
    def run(self):
        threads = []
        for user_id in range(self.num_users):
            t = threading.Thread(target=self._user_transactions, args=(user_id,))
            threads.append(t)
            t.start()

        #this part stops the program from finishing mid-transaction
        #'join()' makes sure that the threads are completed before it proceeds
        for t in threads:
            t.join()
