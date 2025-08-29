#main.py

from bank_account import bankAccount
from transaction import transactionSimulator

def main():
    #Create a shared bank account
    account = bankAccount("ABC123", initial_balance=1000)

    #Run transaction simulator with multiple users
    simulator = transactionSimulator(account, num_users=5, num_transactions=20)
    simulator.run()

    #Final balance check
    print("\n--- Simulation Complete ---")
    print(f"Final Balance in {account.account_number}: {account.get_balance()}")

if __name__ == "__main__":
    main()
