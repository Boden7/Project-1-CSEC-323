# @author Boden Kahn
# Date: 10/8/24
import unittest
from BodensCopy import BankAccount

class TestP1(unittest.TestCase):
    def setUp(self):
        self.testObject = MyClass()

    def testDeposit(self):
        self.testObject.balance = 0.0
        result = self.testObject.deposit(3.0)
        self.assertEqual(result, True)
        self.assertEqual(self.testObject.balance, 3.0)

    def testOverdraft(self):
        self.testObject.balance = 100.0
        result = self.testObject.withdrawl(150.0)
        self.assertEqual(result, True)
        self.assertEqual(self.testObject.balance, -70.0)

    def testFailedDeposit(self):
        self.testObject.balance = -70.0
        result = self.testObject.deposit(-50.0)
        self.assertEqual(result, False)
        self.assertEqual(self.testObject.balance, -70.0)

    def testWithdrawl(self):
        self.testObject.balance = 1000.0
        result = self.testObject.withdrawl(500.0)
        self.assertEqual(result, True)
        self.assertEqual(self.testObject.balance, 500.0)
        
    def testFailedWithdrawl(self):
        self.testObject.balance = 500.0
        result = self.testObject.withdrawl(10000.0)
        self.assertEqual(result, False)
        self.assertEqual(self.testObject.balance, 500.0)

    def testFailedDepositInput(self):
        self.testObject.balance = -70.0
        result = self.testObject.deposit("a")
        self.assertEqual(result, False)
        self.assertEqual(self.testObject.balance, -70.0)
        
    def testFailedWithdrawlInput(self):
        self.testObject.balance = 55.0
        result = self.testObject.withdrawl("a")
        self.assertEqual(result, False)
        self.assertEqual(self.testObject.balance, 55.0)