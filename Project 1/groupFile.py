# @author Anna Pitt
 
#  This module defines the BankAccount class.
#  A class to represent the data elements and methods required to implement a bank account.

# TO DO
# getAccountNumber and NextAccountGetterAndUpdate don't work because I am unsure how to "reset" instances to get everything back to account number 1,000
# We need to add a tester for getOverdrawn when the overdrawn counter is greater than 0
# We need to add testers for non-empty Transaction Lists (both BankAccount and TransactionList)
# We need to add an __eq__ method for both Transaction and BankAccount, if not already done
#

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
   #  @require: balanceIn is a floating-point type
   #
   #  @ensure BankAccount object successfully created
   #  @ensure Overdraft counter set to 0
   def __init__(self, firstIn, lastIn, balanceIn = 0.0):
      # Assert statements for preconditions
      assert firstIn.isalpha(), "The first name must not contain any special characters."
      assert len(firstIn) > 0 and len(firstIn) <= 25, "The first name must be a valid length."
      assert lastIn.isalpha(), "The last name must not contain any special characters."
      assert len(lastIn) > 0 and len(lastIn) <= 40, "The last name must be a valid length."
      
      # Sets the instance variables
      self._firstName = firstIn
      self._lastName = lastIn
      self._accountNum = BankAccount._nextAccountVal
      self._accountTransactions = []
      self._overdrawnCount = 0
      self._balance = balanceIn
      
      # Updates the next account value
      BankAccount._nextAccountVal += 1
   
   # An accessor/getter method for the overdraft fee
   #
   # @return: The overdraft fee (floating-point value)
   def getOverdraft(self):
      return BankAccount._overdraftFee
   
   # An accessor/getter method for the interest rate
   #
   # @return: The interest rate in decimal form (floating-point value)
   def getIntRate(self):
      return BankAccount._intRate
   
   # An accessor/getter method for the next account value
   #
   # @return: The next available account value (integer)
   def getNextAccount(self):
      return BankAccount._nextAccountVal
   
   # An accessor/getter method for the first name
   #
   # @return: The first name associated with the Bank Account (String)
   def getFirst(self):
      return self._firstName
   
   # An accessor/getter method for the last name
   #
   # @return: The last name associated with the Bank Account (String)
   def getLast(self):
      return self._lastName
   
   # An accessor/getter method for the account number
   #
   # @return: The account number associated with the Bank Account (integer)
   def getAccountNumber(self):
      return self._accountNum
   
   # An accessor/getter method for the number of times the account has been
   # overdrawn
   #
   # @return: The overdrawn counter associated with the Bank Account (integer)
   def getOverdrawnCount(self):
      return self._overdrawnCount
   
   # An accessor/getter method for the account balance
   #
   # @return: The account balance associated with the Bank Account (String)
   def getBalance(self):
      return self._balance
   
   # A private mutator/setter method for the overdraft fee
   #
   # @param newFee: The new overdraft fee amount (Floating-point value)
   def _setOverdraft(self, newFee):
      BankAccount._overdraftFee = newFee
      
   # A private mutator/setter method for the interest rate
   #
   # @param newRate: The new interest rate in decimal form (Floating-point value)
   def _setIntRate(self, newRate):
      BankAccount._intRate = newRate
      
   # A mutator/setter method for the first name
   #
   # @param first: The new first name for the Bank Account (String: default is an empty string)
   #
   # @require: first is between 1 and 25 characters inclusive and has no special characters   
   def setFirst(self, first = ""):
      # Assert statements for preconditions
      assert first.isalpha(), "The first name must not contain any special characters."
      assert len(first) > 0 and len(first) <= 25, "The first name must be a valid length."      
      
      self._firstName = first
      
   # A mutator/setter method for the last name
   #
   # @param last: The new last name for the Bank Account (String: default is an empty string)
   #
   # @require: last is between 1 and 40 characters inclusive and has no special characters   
   def setLast(self, last = ""):
      # Assert statements for preconditions
      assert last.isalpha(), "The last name must not contain any special characters."
      assert len(last) > 0 and len(last) <= 40, "The last name must be a valid length."
      
      self._lastName = last
      
   # Returns a String representation of a Bank Account object
   #
   # @return: A String representation of the Bank Account object (String)
   def __repr__(self):
      # Creating the list of valid transactions to print to the screen
      transactionVals = self.transactionList()
      
      return("Bank Account #%d owned by %s %s has a balance of %.2f. The valid transactions include:\n%s" % \
         (self._accountNum, self._firstName, self._lastName, self._balance, transactionVals))
   
   # Returns a String representation of the transactions for a Bank Account object
   #
   # @return: A String representation of the transactions stored within a Bank Account object (String)
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
   
   def calc_interest(self):
        # Hunter
        # Calculate and add interest to the account balance:
        if self.balance > 0:
            interest_amount = self.balance * BankAccount.interest_rate
            transaction = Transaction(interest_amount, "Interest")
            self.transactions.append(transaction)
            self.balance += interest_amount
            return True
        return False
   
   # Transfer an amount of money from one account to anotherS
   def transfer(self, amount, otherAccount):
    if self.withdraw(amount):
        otherAccount.deposit(amount)
        return True
    return False

# test = BankAccount("Sara", "Mathews", 100.0)
#print(test.transactionList())
#print(test)
#test.setFirst("Person")
#test.setLast("Persona")
#test._accountTransactions = [Transaction(1, 100), Transaction(2, 50)]
#print(test.transactionList())
#print(test)
