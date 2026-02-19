# Handle account logic
import json
import os, sys
from decorators import log

# check if account exists
@log
def get_account_by_id_no(id_no):
    file_name = f"accounts/{id_no}.json"

    if not os.path.exists(file_name):
        return None
    
    with open(file_name, "r") as file:
        account = json.load(file)
        print(account)
    return account

@log
def update_account(account):
    id_no = account["id_no"]
    file_name = f"accounts/{id_no}.json"

    if os.path.exists(file_name):
        return None
    
    with open(file_name, "w") as file:
        json.dump(account, file)
    return True

@log
def create_account(id_no, password, name):
    # account_no = "11111"
    # validation
    # id_no, name
    if get_account_by_id_no(id_no):
        #print(f"Account with id no {id_no} already exists.")
        return None

    account = {
        "account_no": id_no,
        "id_no": id_no,
        "name": name,
        "transaction_history": [],
        "balance": 0,
        "password": "123456"
    }

    file_name = f"accounts/{id_no}.json" # saves created account in accounts folder

    with open(file_name, "w") as file:
        json.dump(account, file)
    #print("Account created.")

# create_account(id_no = "223344", name = "Ronnie")
# create_account(id_no = "235355", name = "Nyakwama")
# get_account_by_id_no(id_no = "223344")

#create_account(id_no = "27163117", name = "Kwamboka")