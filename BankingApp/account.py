# Handle account logic
import json
import os
import sys

def create_account(id_no, name):
    # account_no = "11111"
    # validation
    # id_no, name
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
    print("Account created.")

# create_account(id_no = "223344", name = "Ronnie")
# create_account(id_no = "235355", name = "Nyakwama")

# check if account exists
def get_account_by_id_no(id_no):
    file_name = f"accounts/{id_no}.json"

    if not os.path.exists(file_name):
        return None
    
    with open(file_name, "r") as file:
        account = json.load(file)
        print(account)
    return account

get_account_by_id_no(id_no = "223344")