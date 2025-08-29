#tests/test_account.py

import unittest
from bank_account import bankAccount
import threading

class testBankAccount(unittest.TestCase):

    def test_deposit_and_withdraw(self):
        acc = bankAccount("001", 100)
        acc.deposit(50)
        self.assertEqual(acc.get_balance(), 150)
        acc.withdraw(70)
        self.assertEqual(acc.get_balance(), 80)

    def test_concurrent_deposits(self):
        acc = bankAccount("002", 0)

        def deposit_many():
            for _ in range(1000):
                acc.deposit(1)

        threads = [threading.Thread(target=deposit_many) for _ in range(10)]
        for t in threads: t.start()
        for t in threads: t.join()

        self.assertEqual(acc.get_balance(), 10000)

if __name__ == "__main__":
    unittest.main()
