# @author Boden Kahn, Anna Pitt
# Date: 10/11/24
import unittest
from groupFile import BankAccount

class TestP1(unittest.TestCase):
    def setUp(self):
        # Constructs an empty BankAccount object
        # Parameters: First name = "First", Last name = "Last", Balance = 500.0,
        # Account Transactions = [], Overdrawn Count = 0, Account Number = 1000
        self.testObject = BankAccount("First", "Last", 500.0)
        
        # Constructs a valid BankAccount object with no balance parameter
        # Parameters: First name = "First", Last name = "Last", Balance = 0.0,
        # Account Transactions = [], Overdrawn Count = 0, Account Number = 1000        
        self.testObject2 = BankAccount("First", "Last")        

    def test_ConstructorValid(self):
        # Ensures the BankAccount object was made
        self.assertTrue(isinstance(self.testObject, BankAccount))

    def test_ConstructorInvalidFirstNameBlank(self):
        # Ensures the BankAccount object with false call to first name
        # throws an assertion error
        self.assertRaises(AssertionError, BankAccount, "", "Last", "500.0")
        
    def test_ConstructorInvalidFirstNameSpecialChar(self):
        # Ensures the BankAccount object with false call to first name
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "!@#$%", "Last", 500.0)        
    
    def test_ConstructorInvalidFirstNameLength(self):
        # Ensures the BankAccount object with false call to first name
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "aaaaaaaaaaaaaaaaaaaaaaaaaa", "Last", 500.0)        
        
    def test_ConstructorInvalidLastNameBlank(self):
        # Ensures the BankAccount object with false call to last name
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "First", "", 500.0)
    
    def test_ConstructorInvalidLastNameSpecialChar(self):
        # Ensures the BankAccount object with false call to last name
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "First", "!@#$%", 500.0)         
    
    def test_ConstructorInvalidLastNameLength(self):
        # Ensures the BankAccount object with false call to last name
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "First", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 500.0)          
    
    def test_ConstructorInvalidBalance(self):
        # Ensures the BankAccount object with false call to balance
        # throws an assertion error        
        self.assertRaises(AssertionError, BankAccount, "First", "Last", "100.0")           
        
    def test_ConstructorNoBalance(self):        
        # Ensures the BankAccount object was made
        self.assertTrue(isinstance(self.testObject2, BankAccount))
        
        # Ensures the balance was properly set to 0
        self.assertEqual(self.testObject2._balance, 0.0)
    
    def test_OverdraftAccessor(self):
        # Determines the overdraft fee
        fee = self.testObject.getOverdraft()
        
        # Ensures the overdraft fee is properly accessing the private variable holding 20.00
        self.assertEqual(fee, 20.00)
    
    def test_IntRateAccessor(self):
        # Determines the interest rate
        interest = self.testObject.getIntRate()
        
        # Ensures the interest rate is properly accessing the private variable holding 0.075
        self.assertEqual(interest, 0.075)
    
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
        
    def test_getFirst(self):
        # Determines the constructor's stored first name
        firstName = self.testObject.getFirst()
        
        # Ensures the first name was received
        self.assertEqual(firstName, "First")
    
    def test_getLast(self):
        # Determines the constructor's stored last name
        lastName = self.testObject.getLast()
        
        # Ensures the last name was received
        self.assertEqual(lastName, "Last")
    
    def test_getAccountNumberMulti(self):
        # Determines the constructor's stored account number
        accountNum = self.testObject.getAccountNumber()      
        
        # Ensures the account number starts at 1000
        self.assertEqual(accountNum, 1000)
        
        # Determines the second constructor's stored account number
        accountNum2 = self.testObject2.getAccountNumber()
        
        # Ensures the next account number is 1001
        self.assertEqual(accountNum2, 1001)
    
    def test_getOverdrawn(self):
        # Determines the constructor's stored overdrawn counter
        overdrawnCount = self.testObject.getOverdrawnCount()
        
        # Ensures the original overdrawn counter is set to 0
        self.assertEqual(overdrawnCount, 0)
    
    def test_getBalance(self):
        # Determines the constructor's stored balance
        balance = self.testObject.getBalance()
        
        # Ensures the balance is set to 500.0
        self.assertEqual(balance, 500.0)
    
    def test_getBalanceZeroValue(self):
        # Determines the constructor's stored balance
        balance = self.testObject2.getBalance()
        
        # Ensures the balance is set to 0.0
        self.assertEqual(balance, 0.0)
    
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
    
    def test_toStringTransactionListEmpty(self):
        # Determines the String value of a Bank Account object's
        # Transaction List with no transactions.
        strVal = str(self.testObject.transactionList())
        
        # Creates the check for comparing the Bank Account's empty
        # Transaction List.
        strCheck = "There are no valid transactions to display."
        
        # Ensures both values are the same
        self.assertEqual(strVal, strCheck)
        
        
    def testDeposit(self):
        self.testObject.balance = 0.0
        result = self.testObject.deposit(3.0)
        self.assertEqual(result, True)
        self.assertEqual(self.testObject.balance, 3.0)

    def testFailedDeposit(self):
        self.testObject.balance = -70.0
        result = self.testObject.deposit(-50.0)
        self.assertEqual(result, False)
        self.assertEqual(self.testObject.balance, -70.0)

    def testFailedDepositInput(self):
        self.testObject.balance = -70.0
        result = self.testObject.deposit("a")
        self.assertEqual(result, False)
        self.assertEqual(self.testObject.balance, -70.0)


    def testOverdraft(self):
        self.testObject.balance = 100.0
        result = self.testObject.withdrawal(150.0)
        self.assertEqual(result, True)
        self.assertEqual(self.testObject.balance, -70.0)

    def testOverdrawnCount(self):
        self.assertEqual(self.testObject.getOverdrawnCount(), 1)
        self.testObject.balance = 40.0
        result = self.testObject.withdrawal(150.0)
        self.assertEqual(self.testObject.getOverdrawnCount(), 2)

    def testWithdrawal(self):
        self.testObject.balance = 1000.0
        result = self.testObject.withdrawal(500.0)
        self.assertEqual(result, True)
        self.assertEqual(self.testObject.balance, 500.0)
        
    def testFailedWithdrawal(self):
        self.testObject.balance = 500.0
        result = self.testObject.withdrawal(10000.0)
        self.assertEqual(result, False)
        self.assertEqual(self.testObject.balance, 500.0)
        
    def testFailedWithdrawalInput(self):
        self.testObject.balance = 55.0
        result = self.testObject.withdrawal("a")
        self.assertEqual(result, False)
        self.assertEqual(self.testObject.balance, 55.0)
if __name__ == '__main__':
    unittest.main()
