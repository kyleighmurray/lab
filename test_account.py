import unittest
import account

class TestAccount(unittest.TestCase):
    
    def test_deposit(self):

        ex1 = account.Account('ex')
        
        self.assertTrue(ex1.deposit(100))
        self.assertTrue(ex1.deposit(0.2))
        self.assertFalse(ex1.deposit(0))
        self.assertFalse(ex1.deposit(-1))
        self.assertFalse(ex1.deposit(-2.2))

    def test_withdraw(self):

        ex2 = account.Account('ex')
        
        ex2.deposit(100.2)
        
        self.assertTrue(ex2.withdraw(100))
        self.assertFalse(ex2.withdraw(100))
        self.assertTrue(ex2.withdraw(.2))
        self.assertFalse(ex2.withdraw(0))
        self.assertFalse(ex2.withdraw(-1))
        self.assertFalse(ex2.withdraw(-2.2))

    def test_get_balance(self):

        ex3 = account.Account('ex')
        
        self.assertEqual(ex3.get_balance(), 0)
        
        ex3.deposit(3)
        
        self.assertEqual(ex3.get_balance(), 3)
        
        ex3.deposit(.4)
        
        self.assertEqual(ex3.get_balance(), 3.4)

    def test_get_name(self):

        ex4 = account.Account('John Doe')
        ex5 = account.Account('!@#%^&')
        ex6 = account.Account('0')
        
        self.assertEqual(ex4.get_name(), 'John Doe')
        self.assertEqual(ex5.get_name(), '!@#%^&')
        self.assertEqual(ex6.get_name(), '0')


if __name__ == '__main__':
    unittest.main()
