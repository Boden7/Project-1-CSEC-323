# @author Boden Kahn, Anna Pitt
# Date: 10/11/24
import unittest
from groupFile import BankAccount

class TestP1(unittest.TestCase):
    # Anna
    def setUp(self):
        #Resets the bank account number for each test
        BankAccount._nextAccountVal = 1000
        # Constructs an empty BankAccount object
        # Parameters: First name = "First", Last name = "Last", Balance = 500.0,
        # Account Transactions = [], Overdrawn Count = 0, Account Number = 1000
        self.testObject = BankAccount("First", "Last", 500.0)
        
        # Constructs a valid BankAccount object with no balance parameter
        # Parameters: First name = "First", Last name = "Last", Balance = 0.0,
        # Account Transactions = [], Overdrawn Count = 0, Account Number = 1001        
        self.testObject2 = BankAccount("First", "Last")        

        def test_ConstructorValid(self):
        # Ensures the BankAccount object was made
        self.assertTrue(isinstance(self.testObject, BankAccount))

    # Anna
    def test_ConstructorInvalidFirstNameBlank(self):
        # Ensures the BankAccount object with false call to first name
        # throws an assertion error
        self.assertRaises(AssertionError, BankAccount, "", "Last", "500.0")

    # Anna
    def test_ConstructorInvalidFirstNameSpecialChar(self):
        # Ensures the BankAccount object with false call to first name
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "!@#$%", "Last", 500.0)        
    
    # Anna
    def test_ConstructorInvalidFirstNameLength(self):
        # Ensures the BankAccount object with false call to first name
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "aaaaaaaaaaaaaaaaaaaaaaaaaa", "Last", 500.0)
        
    # Anna
    def test_ConstructorInvalidLastNameBlank(self):
        # Ensures the BankAccount object with false call to last name
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "First", "", 500.0)
    
    # Anna
    def test_ConstructorInvalidLastNameSpecialChar(self):
        # Ensures the BankAccount object with false call to last name
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "First", "!@#$%", 500.0)         

    # Anna
    def test_ConstructorInvalidLastNameLength(self):
        # Ensures the BankAccount object with false call to last name
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "First", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 500.0)          

    # Anna
    def test_ConstructorInvalidBalanceType(self):
        # Ensures the BankAccount object with false call to balance
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "First", "Last", "100.0")

    # Anna
    def test_ConstructorInvalidBalanceAmount(self):
        # Ensures the BankAccount object with false call to balance
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "First", "Last", -500.0)    

    # Anna
    def test_ConstructorNoBalance(self):        
        # Ensures the BankAccount object was made
        self.assertTrue(isinstance(self.testObject2, BankAccount))
        
        # Ensures the balance was properly set to 0
        self.assertEqual(self.testObject2._balance, 0.0)

    # Anna
    def test_OverdraftAccessor(self):
        # Determines the overdraft fee
        fee = self.testObject.getOverdraft()
        
        # Ensures the overdraft fee is properly accessing the private variable holding 20.00
        self.assertEqual(fee, 20.00)

    # Anna
    def test_IntRateAccessor(self):
        # Determines the interest rate
        interest = self.testObject.getIntRate()
        
        # Ensures the interest rate is properly accessing the private variable holding 0.075
        self.assertEqual(interest, 0.075)

    # Anna
    def test_NextAccountGetterAndUpdate(self):
        # Determines the starting available account number
        nextAccount = self.testObject.getNextAccount()
        
        # Ensures that the first available account number starts at 1000
        self.assertTrue(nextAccount, 1000)
        
        # Determines the next available account number after an instance was
        # created
        nextAccount2 = self.testObject2.getNextAccount()
        
        # Ensures that the next available account number is 1001        
        self.assertTrue(nextAccount2, 1001)

    # Anna
    def test_getFirst(self):
        # Determines the constructor's stored first name
        firstName = self.testObject.getFirst()
        
        # Ensures the first name was received
        self.assertEqual(firstName, "First")

    # Anna
    def test_getLast(self):
        # Determines the constructor's stored last name
        lastName = self.testObject.getLast()
        
        # Ensures the last name was received
        self.assertEqual(lastName, "Last")

    # Anna
    def test_getAccountNumberMulti(self):
        # Determines the constructor's stored account number
        accountNum = self.testObject.getAccountNumber()      
        
        # Ensures the account number starts at 1000
        self.assertEqual(accountNum, 1000)
        
        # Determines the second constructor's stored account number
        accountNum2 = self.testObject2.getAccountNumber()
        
        # Ensures the next account number is 1001
        self.assertEqual(accountNum2, 1001)

    # Anna
    def test_getOverdrawnZero(self):
        # Determines the constructor's stored overdrawn counter (with no 
        # transactions, should be initialized to 0)
        overdrawnCount = self.testObject.getOverdrawnCount()
        
        # Ensures the original overdrawn counter is set to 0
        self.assertEqual(overdrawnCount, 0)

    # Anna
    def test_getBalance(self):
        # Determines the constructor's stored balance
        balance = self.testObject.getBalance()
        
        # Ensures the balance is set to 500.0
        self.assertEqual(balance, 500.0)

    # Anna
    def test_getBalanceZeroValue(self):
        # Determines the constructor's stored balance
        balance = self.testObject2.getBalance()
        
        # Ensures the balance is set to 0.0
        self.assertEqual(balance, 0.0)

    # Anna
    def test_setFirstValid(self):
        # Changes the first name to a valid new name
        self.testObject.setFirst("FirstNew")
        
        # Accesses the first name
        firstCheck = self.testObject.getFirst()
        
        # Ensures that the first name was correctly updated
        self.assertEqual(firstCheck, "FirstNew")

    # Anna
    def test_setFirstInvalidFirstNameBlank(self):
        # Ensures the BankAccount object with false call to changing first name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.testObject.setFirst, "")

    # Anna
    def test_setFirstInvalidFirstNameSpecialChar(self):
        # Ensures the BankAccount object with false call to changing first name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.testObject.setFirst, "!@#$%")        

    # Anna
    def test_setFirstInvalidFirstNameNameLength(self):
        # Ensures the BankAccount object with false call to changing first name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.testObject.setFirst, "aaaaaaaaaaaaaaaaaaaaaaaaaa")

    # Anna
    def test_setLastValid(self):
        # Changes the last name to a valid new name
        self.testObject.setLast("LastNew")
        
        # Accesses the last name
        lastCheck = self.testObject.getLast()
        
        # Ensures that the last name was correctly updated
        self.assertEqual(lastCheck, "LastNew")    

    # Anna
    def test_setLastInvalidLastNameBlank(self):
        # Ensures the BankAccount object with false call to changing last name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.testObject.setLast, "")

    # Anna
    def test_setLastInvalidLastNameSpecialChar(self):
        # Ensures the BankAccount object with false call to changing last name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.testObject.setLast, "!@#$%")         

    # Anna
    def test_setLastInvalidLastNameLength(self):
        # Ensures the BankAccount object with false call to changing last name
        # throws an assertion error        
        self.assertRaises(AssertionError, self.testObject.setLast, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    # Anna
    def test_setOverdraftValid(self):
        # Changes the overdraft fee to a valid new overdraft fee
        self.testObject._setOverdraft(15.00)
        
        # Accesses the overdraft fee
        overdraftCheck = self.testObject.getOverdraft()
        
        # Ensures that the overdraft fee was correctly updated
        self.assertEqual(overdraftCheck, 15.00)

    # Anna
    def test_setOverdraftInvalidType(self):
        # Ensures the BankAccount object with false call to changing overdraft
        # fee throws an assertion error        
        self.assertRaises(AssertionError, self.testObject._setOverdraft, "15.00")

    # Anna
    def test_setOverdraftInvalidAmount(self):
        # Ensures the BankAccount object with false call to changing overdraft
        # fee throws an assertion error        
        self.assertRaises(AssertionError, self.testObject._setOverdraft, -15.00)

    # Anna
    def test_setIntRateValid(self):
        # Changes the interest rate to a valid new interest rate
        self.testObject._setIntRate(0.10)
        
        # Accesses the interest rate
        interestCheck = self.testObject.getIntRate()
        
        # Ensures that the interest rate was correctly updated
        self.assertEqual(interestCheck, 0.10)  

    # Anna
    def test_setIntRateInvalidType(self):
        # Ensures the BankAccount object with false call to changing interest
        # rate throws an assertion error        
        self.assertRaises(AssertionError, self.testObject._setIntRate, "0.10")

    # Anna
    def test_setIntRateInvalidPercentHigh(self):
        # Ensures the BankAccount object with false call to changing interest
        # rate throws an assertion error        
        self.assertRaises(AssertionError, self.testObject._setIntRate, 15.00)

    # Anna
    def test_setIntRateInvalidPercentZero(self):
        # Ensures the BankAccount object with false call to changing interest
        # rate throws an assertion error        
        self.assertRaises(AssertionError, self.testObject._setIntRate, 0.0)     

    # Anna
    def test_toStringBankAccountEmpty(self):
        # Determines the String value of a Bank Account object
        # with no transactions.
        strVal = str(self.testObject)
        
        # Determines the String value that should be printed from an empty
        # Bank Account object with the following parameters:
        # Parameters: First name = "First", Last name = "Last", Balance = 500.0,
        # Account Transactions = [], Overdrawn Count = 0, Account Number = 1000
        strCheck = "Bank Account #1000 owned by First Last has a balance of 500.00. The valid transactions include:\nThere are no valid transactions to display."
        
        # Ensures both values are the same
        self.assertEqual(strVal, strCheck)

    # Anna
    def test_toStringTransactionListEmpty(self):
        # Determines the String value of a Bank Account object's
        # Transaction List with no transactions.
        strVal = str(self.testObject.transactionList())
        
        # Creates the check for comparing the Bank Account's empty
        # Transaction List.
        strCheck = "There are no valid transactions to display."
        
        # Ensures both values are the same
        self.assertEqual(strVal, strCheck)

    # Boden
    # Tests to see if the interest application works under normal conditions
    def testInterest(self):
        # Initalize balance to be greater than 0
        self.testObject._balance = 100.0
        # Make sure the interest addition is successful
        self.assertEqual(self.testObject.calc_interest(), True)
        # Make sure the balance did update to the correct amount
        self.assertEqual(self.testObject.getBalance(), 107.5)

    # Boden
    # Tests to see if the interest application fails when preconditions aren't met
    def testInterestFailed(self):
        # Initalize balance to be  0
        self.testObject._balance = 0
        # Make sure the interest addition is not successful
        self.assertEqual(self.testObject.calc_interest(), False)
        # Make sure the balance did not update
        self.assertEqual(self.testObject.getBalance(), 0)

    # Boden
    # Tests the transfer method to ensure everything works under proper conditions
    def testTransfer(self):
        # Initalize balance of account 1 to be 1000
        self.testObject._balance = 1000.0
        # Initalize balance of account 2 to be 700
        self.testObject2._balance = 700.0
        # Attempt the transfer for a valid amount
        result = self.testObject.transfer(500.0, self.testObject2)
        # Ensure the transfer was successful
        self.assertEqual(result, True)
        # Ensure the balance is correctly updated for account 1
        self.assertEqual(self.testObject.getBalance(), 500.0)
        # Ensure the balance is correctly updated for account 2
        self.assertEqual(self.testObject2.getBalance(), 1200.0)

    # Boden
    # Tests the transfer method to ensure method reject
    def testTransferFailed(self):
        # Initalize balance of account 1 to be 1000
        self.testObject._balance = 1000.0
        # Initalize balance of account 2 to be 700
        self.testObject2._balance = 700.0
        # Attempt the transfer for a valid amount
        result = self.testObject.transfer(10000.0, self.testObject2)
        # Ensure the transfer was not successful
        self.assertEqual(result, False)
        # Ensure the balance is not updated for account 1
        self.assertEqual(self.testObject.getBalance(), 1000.0)
        # Ensure the balance is not updated for account 2
        self.assertEqual(self.testObject2.getBalance(), 700.0)

    # Boden
    # Tests the transfer method to ensure method reject
    def testTransferFailedInput(self):
        # Initalize balance of account 1 to be 1000
        self.testObject._balance = 1000
        # Initalize balance of account 2 to be 700
        self.testObject2._balance = 700
        # Attempt the transfer for a valid amount
        result = self.testObject.transfer("A", 37)
        # Ensure the transfer was not successful
        self.assertEqual(result, False)
        # Ensure the balance is not updated for account 1
        self.assertEqual(self.testObject.getBalance(), 1000)
        # Ensure the balance is not updated for account 2
        self.assertEqual(self.testObject2.getBalance(), 700)


    # Boden
    # Tests the deposit method to ensure it functions normally    
    def testDeposit(self):
        # Initialize balance to 0
        self.testObject._balance = 0.0
        # Add three to the balance
        result = self.testObject.deposit(3.0)
        # Ensure the deposit was successful
        self.assertEqual(result, True)
        # Ensure the balance is correctly updated
        self.assertEqual(self.testObject.getBalance(), 3.0)

    # Boden
    # Tests the deposit method to ensure it rejects an incorrect input (number)
    def testFailedDeposit(self):
        # Set the balance to a valid number
        self.testObject._balance = -70.0
        # Attempt to deposit a negative number
        result = self.testObject.deposit(-50.0)
        # Ensure the deposit did not occur
        self.assertEqual(result, False)
        # Ensure the balance remained unchanged
        self.assertEqual(self.testObject.getBalance(), -70.0)

    # Boden
    # Tests the deposit method to ensure it rejects an incorrect input (string)
    def testFailedDepositInput(self):
        # Set the balance to a valid number
        self.testObject._balance = -70.0
        # Attempt to deposit a string
        result = self.testObject.deposit("a")
        # Ensure the deposit did not occur
        self.assertEqual(result, False)
        # Ensure the balance remained unchanged
        self.assertEqual(self.testObject.getBalance(), -70.0)

    # Boden
    def testOverdraft(self):
        # Set the balance to a valid number
        self.testObject._balance = 100.0
        # Attempt to withdraw a valid amount that will cause an overdraft
        result = self.testObject.withdraw(150.0)
        # Ensure the withdrawal was successful
        self.assertEqual(result, True)
        # Ensure the balance was updated correctly
        self.assertEqual(self.testObject.getBalance(), -70.0)

    # Boden
    def testOverdrawnCount(self):
        # Ensure overdraft counter is 0
        self.assertEqual(self.testObject.getOverdrawnCount(), 0)
        # Set the balance to a valid number
        self.testObject._balance = 40.0
        # Attempt to withdraw a valid amount that will cause an overdraft
        self.testObject.withdraw(150.0)
        # Ensure overdraft counter is updated
        self.assertEqual(self.testObject.getOverdrawnCount(), 1)

    # Boden
    def testWithdrawal(self):
        # Set the balance to a valid number
        self.testObject._balance = 1000.0
        # Attempt to withdraw a valid amount that will not cause an overdraft
        result = self.testObject.withdraw(500.0)
        # Ensure the withdrawal was successful
        self.assertEqual(result, True)
        # Ensure the balance was updated correctly
        self.assertEqual(self.testObject.getBalance(), 500.0)

    # Boden
    def testFailedWithdrawal(self):
        # Set the balance to a valid number
        self.testObject._balance = 500.0
        # Attempt to withdraw an invalid amount
        result = self.testObject.withdraw(10000.0)
        # Ensure the withdrawal was unsuccessful
        self.assertEqual(result, False)
        # Ensure the balance was not updated
        self.assertEqual(self.testObject.getBalance(), 500.0)

    # Boden
    def testFailedWithdrawalInput(self):
        # Set the balance to a valid number
        self.testObject._balance = 55.0
        # Attempt to withdraw with an invalid input
        result = self.testObject.withdraw("a")
        # Ensure the withdrawal was unsuccessful
        self.assertEqual(result, False)
        # Ensure the balance was not updated
        self.assertEqual(self.testObject.getBalance(), 55.0)

    # Anna
    def test_equalityEquals(self):
        # Checks if the equality method works on two objects that are the same
        # (both have the same Account Number)
        self.assertTrue(self.testObject == self.testObject)

    # Anna
    def test_equalityNotEquals(self):
        # Checks if the equality method works on two objects that are different
        # (both do not have the same Account Number)
        self.assertFalse(self.testObject == self.testObject2)  

if __name__ == '__main__':
    unittest.main()
