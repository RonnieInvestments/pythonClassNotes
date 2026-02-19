# Deposit, withdraw, account opening, and balance logic
from account import create_account, get_account_by_id_no, update_account
from decorators import log
from time import sleep
from datetime import datetime

@log
def new_account(trials = 0):

    if trials > 3:
        print("Maximum trials. Exiting...")
        return None
    
    print("Welcome to Prime Bank.")
    print("Create Account")
    id_no = input("Enter id no:\n")
    account = get_account_by_id_no(id_no)

    if account:
        seconds = trials + 2
        print(f"Id number already in use. Try again in {seconds}s.")
        sleep(seconds)
        new_account(trials = trials + 1)
        return
    
    name = input("Enter name:\n")
    password = input("Enter your password:\n")
    account = create_account(name = name, password = password, id_no = id_no)

    if account:
        print(f"Welcome {account["name"]}. Account created.")
    return account
    
#new_account()
# Deposit function
@log
def deposit(account):
    transaction_history = account["transaction_history"]
    balance = account["balance"]
    print(f"Account balance is {balance}.")
    amount = int(input("Deposit Amount"))

    # try-except -> for string inputs
    # Additional check if amount > 0
    if amount < 0:
        print("To deposit, please enter amount greater than 0.")
        return None
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_balance = balance + amount
    transaction_history.append({
            "transaction_type":"Deposit",
            "timestamp": timestamp,
            "amount": amount,
            "balance": balance,
            "new_balance": new_balance
        })
    account["balance"] = new_balance
    account["transaction_history"] = transaction_history

    account_update = update_account(account = account)
    return account_update

account = get_account_by_id_no("234567")
deposit(account)