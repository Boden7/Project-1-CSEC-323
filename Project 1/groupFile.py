# @author Anna Pitt
 
#  This module defines the BankAccount class.
#  A class to represent the data elements and methods required to implement a bank account.

# Import statements
from transaction import Transaction

class BankAccount:
   # A private class variable that holds the number of the next account value
   _nextAccountVal = 1000
   
   # A private class variable that holds the overdraft fee amount
   _overdraftFee = 20.00
   
   # A private class variable that holds the interest rate in decimal form
   _intRate = 0.075
   
   # Constructs a BankAccount object.
   #
   #  @param firstIn: The first name of the Bank Account holder (String)
   #  @param lastIn: The last name of the Bank Account holder (String)
   #  @param balanceIn: The starting balance of the Bank Account (Floating point: Default is $0)
   #
   #  @require: firstIn is between 1 and 25 characters inclusive and has no special characters
   #  @require: lastIn is between 1 and 40 characters inclusive and has no special characters
   #  @require: balanceIn is a floating-point type and is positive
   #
   #  @ensure BankAccount object successfully created
   #  @ensure Overdraft counter set to 0
   # Anna
   def __init__(self, firstIn, lastIn, balanceIn = 0.0):
      # Assert statements for preconditions
      assert firstIn.isalpha(), "The first name must not contain any special characters."
      assert len(firstIn) > 0 and len(firstIn) <= 25, "The first name must be a valid length."
      assert lastIn.isalpha(), "The last name must not contain any special characters."
      assert len(lastIn) > 0 and len(lastIn) <= 40, "The last name must be a valid length."
      assert isinstance(balanceIn, float), "The balance must be a floating-point value."
      assert balanceIn >= 0.0, "The balance must be a positive value."
      
      # Sets the instance variables
      self._firstName = firstIn
      self._lastName = lastIn
      self._accountNum = BankAccount._nextAccountVal
      self._accountTransactions = [] # Container that stores all transactions
      self._overdrawnCount = 0 # Counter for how many times an account is overdawn
      self._balance = balanceIn
      
      # Updates the next account value
      BankAccount._nextAccountVal += 1
   
   # An accessor/getter method for the overdraft fee
   #
   # @return: The overdraft fee (floating-point value)
   # Anna
   def getOverdraft(self):
      return BankAccount._overdraftFee
   
   # An accessor/getter method for the interest rate
   #
   # @return: The interest rate in decimal form (floating-point value)
   # Anna
   def getIntRate(self):
      return BankAccount._intRate
   
   # An accessor/getter method for the next account value
   #
   # @return: The next available account value (integer)
   # Anna
   def getNextAccount(self):
      return BankAccount._nextAccountVal
   
   # An accessor/getter method for the first name
   #
   # @return: The first name associated with the Bank Account (String)
   # Anna
   def getFirst(self):
      return self._firstName
   
   # An accessor/getter method for the last name
   #
   # @return: The last name associated with the Bank Account (String)
   # Anna
   def getLast(self):
      return self._lastName
   
   # An accessor/getter method for the account number
   #
   # @return: The account number associated with the Bank Account (integer)
   # Anna
   def getAccountNumber(self):
      return self._accountNum
   
   # An accessor/getter method for the number of times the account has been
   # overdrawn
   #
   # @return: The overdrawn counter associated with the Bank Account (integer)
   # Anna
   def getOverdrawnCount(self):
      return self._overdrawnCount
   
   # An accessor/getter method for the account balance
   #
   # @return: The account balance associated with the Bank Account (String)
   # Anna
   def getBalance(self):
      return self._balance
   
   # A private mutator/setter method for the overdraft fee
   #
   # @param newFee: The new overdraft fee amount (Floating-point value)
   #
   # @require: newFee is a positive value that is an instance of a float
   # Anna
   def _setOverdraft(self, newFee):
      # Assert statements for preconditions
      assert isinstance(newFee, float), "The overdraft fee must be a floating-point value."
      assert newFee > 0, "The overdraft fee must be a positive value."
    
      BankAccount._overdraftFee = newFee
      
   # A private mutator/setter method for the interest rate
   #
   # @param newRate: The new interest rate in decimal form (Floating-point value)
   #
   # @require: newRate is a positive value between 0 (exclusive) and 1 (inclusive) that is an instance of a float
   # Anna
   def _setIntRate(self, newRate):
      BankAccount._intRate = newRate
      
   # A mutator/setter method for the first name
   #
   # @param first: The new first name for the Bank Account (String: default is an empty string)
   #
   # @require: first is between 1 and 25 characters inclusive and has no special characters   
   # Anna
   def setFirst(self, first):
      # Assert statements for preconditions
      assert first.isalpha(), "The first name must not contain any special characters."
      assert len(first) > 0 and len(first) <= 25, "The first name must be a valid length."      
      
      self._firstName = first
      
   # A mutator/setter method for the last name
   #
   # @param last: The new last name for the Bank Account (String: default is an empty string)
   #
   # @require: last is between 1 and 40 characters inclusive and has no special characters   
   # Anna
   def setLast(self, last):
      # Assert statements for preconditions
      assert last.isalpha(), "The last name must not contain any special characters."
      assert len(last) > 0 and len(last) <= 40, "The last name must be a valid length."
      
      self._lastName = last
      
   # Returns a String representation of a Bank Account object
   #
   # @return: A String representation of the Bank Account object (String)
   # Anna
   def __repr__(self):
      # Creating the list of valid transactions to print to the screen
      transactionVals = self.transactionList()
      
      return("Bank Account #%d owned by %s %s has a balance of %.2f. The valid transactions include:\n%s" % \
         (self._accountNum, self._firstName, self._lastName, self._balance, transactionVals))
   
   # Returns a String representation of the transactions for a Bank Account object
   #
   # @return: A String representation of the transactions stored within a Bank Account object (String)
   # Anna
   def transactionList(self):
      # If the transaction list is empty
      if(len(self._accountTransactions) == 0):
         return("There are no valid transactions to display.")
      
      # If there is at least one transaction in the transaction list to display
      else:
         # Creates a String variable to hold the list of transactions
         transList = ""
         
         # Loops through every transaction in the list
         for transIndex in range(len(self._accountTransactions)):
            
            # If the transaction is the last one in the list
            if(transIndex == (len(self._accountTransactions) - 1)):
               # Adds the String representation of the transaction to transList (without a new line)
               transList = transList + str(self._accountTransactions[transIndex])
               
            # If the transaction is not the last one in the list
            else:
               # Adds the String representation of the transaction to transList (with a new line)
               transList = transList + str(self._accountTransactions[transIndex]) + "\n"
      
      # Returns the full amount of transactions as a String
      return(transList)
   
   # Calculates the interest payment for an account, adds a new interest transaction
   # to the account, and updates the account balance
   # @require amount > 0
   # @return if the interest was added or not
   # Hunter
   def calc_interest(self):
        
        # Calculate and add interest to the account balance:
        if self._balance > 0:
            interest_amount = self._balance * BankAccount._intRate
            transaction = Transaction("interest", interest_amount)
            # add interest to list of transactions
            self._accountTransactions.append(transaction)
            self._balance += interest_amount
            return True
        return False
   
   # Transfer an amount of money from one account to another
   # @param amount: The amount being transferred to the other account
   # @param otherAccount: The account that is being transferred the money (if possible)
   # @return: True if the money was able to be transferred and False if not
   # Brenden
   def transfer(self, amount, otherAccount):
    if self.withdraw(amount):
        otherAccount.deposit(amount)
        transaction = Transaction("transfer", amount)
        # add transfer to list of transactions
        self._accountTransactions.append(transaction)
        return True
    return False

   # Deposits money into the account if the transaction is valid and records the transaction
   # Boden
   #@param amount: the amount to be deposited
   #@require amount > 0
   #@return The success or failure of the deposit
   def deposit(self, amount):
       # Make sure the amount to deposit is not negative
       if isinstance(amount, float) and amount > 0:
           # Process the transaction and update necessary variables
           depositTransaction = Transaction("deposit", amount)
           # add deposit to list of transactions
           self._accountTransactions.append(depositTransaction)
           self._balance += amount
           return True
       # If anything was wrong with the amount parameter the transaction will be rejected
       return False

   # Withdrawals money from the account if the transaction is valid and records the transaction; 
   # If the transaction is valid but the account will be overdrawn, applies an overdraft fee and 
   # updates the counter for overdraws
   # Boden
   #@param amount: the amount to be withdrawn
   #@require amount > 0
   #@return The success or failure of the withdrawal
   def withdraw(self, amount):
       # Make sure the amount to withdrawal is not negative
       if isinstance(amount, float) and amount <= 0:
           print("Transaction denied.")
       # Ensure the balance is at least $250 more than the withdrawal amount
       if isinstance(amount, float) and amount < self.getBalance() + 250.0:
           # Process the transaction and update necessary variables
           withdrawalTransaction = Transaction("withdrawal", amount)
           # add withdrawal to list of transactions
           self._accountTransactions.append(withdrawalTransaction)
           self._balance -= amount
           # If the withdrawal would put the balance in the negative, add an
           # overdraft fee and increment the overdrawn counter
           if self.getBalance() < 0.0:
               # Process the transaction and update necessary variables
               self._balance -= self.getOverdraft()
               penaltyTransaction = Transaction("penalty", self.getOverdraft())
               # add penalty to list of transactions
               self._accountTransactions.append(penaltyTransaction)
               self._overdrawnCount = self.getOverdrawnCount() + 1 
               print("The account is overdrawn")
           return True
       # If the amount parameter was anything other than a number the transaction will be rejected
       else:
           print("Transaction denied")
       return False

   # Compares two Bank Accounts to see if they are the same
   #
   # @param otherAccount: The account to compare the original Bank Account (self) to
   #
   # @return: True if the two Bank Accounts are equal, False if not
   def __eq__(self, otherAccount):
   # Compares the immutable variables of both Bank Accounts to test for
   # equality
       if(self._accountNum == otherAccount._accountNum):
          return True
       # If the comparisons aren't equal, then the Bank Accounts are not the same
       else:
          return False
