# @author Boden Kahn
# Date: 10/8/24
# Project 1

from transaction import Transaction

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.overdraft = 20
        self.overdrawnCount = 0
        self.transactions = []

    # Deposits money into the account if the transaction is valid and records the transaction
    #@param amount: the amount to be deposited
    #@require amount is a number
    #@return The success or failure of the deposit
    def deposit(self, amount):
        # Make sure the amount to deposit is not negative
        if isinstance(amount, float) and amount > 0:
            # Process the transaction and update necessary variables
            depositTransaction = Transaction("deposit", amount)
            self.transactions.append(depositTransaction)
            self.balance += amount
            return True
        # If anything was wrong with the amount parameter the transaction will be rejected
        return False

    # Withdrawls money from the account if the transaction is valid and records the transaction; 
    # If the transaction is valid but the account will be overdrawn, applies an overdraft fee and 
    # updates the counter for overdraws
    #@param amount: the amount to be withdrawn
    #@require amount > 0
    #@return The success or failure of the withdrawl
    def withdrawl(self, amount):
        # Make sure the amount to withdrawl is not negative
        if isinstance(amount, float) and amount <= 0:
            print("Transaction denied.")
        # Ensure the balance is at least $250 more than the withdrawl amount
        if isinstance(amount, float) and amount < self.balance + 250.0:
            # Process the transaction and update necessary variables
            withdrawlTransaction = Transaction("withdrawl", amount)
            self.transactions.append(withdrawlTransaction)
            self.balance -= amount
            # If the withdrawl would put the balance in the negative, add an
            # overdraft fee and increment the overdrawn counter
            if self.balance < 0.0:
                # Process the transaction and update necessary variables
                self.balance -= self.overdraft
                penaltyTransaction = Transaction("penalty", self.overdraft)
                self.transactions.append(penaltyTransaction)
                self.overdrawnCount += 1
                print("The account is overdrawn")
            return True
        # If the amount parameter was anything other than a number the transaction will be rejected
        else:
            print("Transaction denied")
        return False