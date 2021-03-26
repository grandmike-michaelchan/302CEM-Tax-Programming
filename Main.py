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
    print("\n")
    income = int(input("Input Income: "))
    if income > 360000:
        mpf = 18000
    elif income < 360000:  
        mpf = income * 5/100
    print("The MPF allowance is: ", mpf)
    standard = (income - mpf)*15/100
    print("Standard Rate Tax Total: ", standard)

def main(argv):
        print("Welcome to Tax Calculator")
        print("-------- Menu -------")
        print("1. Run single tax calulation")
        print("2. Run marriage tax calculation")
        print("3. run the testing ")
        choice = int(input ("Enter number: "))

        if choice == 1:
            single()

        if choice == 2:
            test()
            

if __name__ == "__main__":
    main(sys.argv)