# Bank Account -> name, balance, repr method for bank account

class Bank_Account:
    # This is a constructor method:
        # runs automatically when a new Bank_Account object is created
        # initializes the account holder's name and starting balance
    
    def __init__(self, name, balance):
        self.name = name # Stores account name
        self._balance = balance # Stores balance

    # Getter and Setter Methods
    def get_balance(self):
        return self.get_balance
    
    def set_balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative.")
        else:
            self._balance = amount

    # Property method
    balance = property(get_balance, set_balance)

    # Deposit function -> Adds amount to account
    def deposit(self, amount_to_deposit):
        # Check if amount is negative
        if amount_to_deposit <= 0:
            print("Enter amount greater than zero.")
        # If amount is more than zero proceed
        else:
            self.balance += amount_to_deposit
            print(f"Successfully deposit of {amount_to_deposit:.2f}")

    # Withdrawal function -> Substracts amount from account
    def withdraw(self, amount_to_withdraw):
        # Check if amount is negative
        if amount_to_withdraw <= 0:
            print("Enter amount greater than zero.")
        # Check if amount is equal to or more than balance
        elif amount_to_withdraw > self.balance:
            print("Please enter an amount less than or equal to your balance")
            print(f"Your current balance is {self.balance}.")
        # Proceed to execution
        else:
            self.balance -= amount_to_withdraw
            print(f"Successful withdrawal of {amount_to_withdraw:.2f}")

    # The __repr__ method defines object representation
        # It returns a formatted string showing the account details.
    def __repr__(self):
        return f"BankAccount(name='{self.name}', balance={self.balance:.2f})"
    
# ronaldo = Bank_Account("Ronaldo", 5000)
# print(ronaldo)

