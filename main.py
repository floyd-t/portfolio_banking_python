#main.py

#imports classes from other files
from bank_account import bankAccount
from transaction import transactionSimulator

#creates bank account and designates number of users and transactions
def main():
    #create a bank account
    account = bankAccount("123456", initial_balance=1000)

    #run transaction simulator with multiple users
    #the number of transactions is per account (user 1 will have 20 transactions)
    simulator = transactionSimulator(account, num_users=5, num_transactions=20)
    simulator.run()

    #final balance check
    print("\n")
    print("Simulation Complete")
    print(f"Final Balance in {account.account_number}: {account.get_balance()}")

#makes it so that the results are only shown if ran from 'main.py'
if __name__ == "__main__":
    main()
