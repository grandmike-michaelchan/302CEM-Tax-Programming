import unittest
import sys
import math


class AddTestCase(unittest.TestCase):
    def setUp(self):
        # The initialise value, tax amount here ...
        self.args = (100, 99)

    def tearDown(self):
        self.args = None

    def test_add(self):
        # The tax calculated value by hand
        expected = 199;
        result = add(*self.args);
        print("The result is: ", result)
        # assertEqual = Compare the diffrence between expected and actual result        
        self.assertEqual(expected, result);

# Functions to be tested, tax formula 
def add(x, y):
    return x + y

def test():
    # TestSuite means Test Case 
    suite = unittest.TestSuite()
    # Call to run the test case 
    suite.addTest(AddTestCase('test_add'))
    # verbosity 是調整執行測試時所輸出的細節
    unittest.TextTestRunner(verbosity=2).run(suite)

def single():
    print("Single Tax Calculation")
    income = int(input("Input Income"))
    mpf = int(input("Input MPF"))

def main(argv):
        print("Welcome to Tax Calculator")
        print("-------- Menu -------")
        print("1. Run single tax calulation")
        print("2. Run marriage tax calculation")
        print("3. run the testing ")
        choice = int(input ("Enter number: "))

        if choice == 1:
            print("Hello")
            single()

        if choice == 2:
            test()
            

if __name__ == "__main__":
    main(sys.argv)