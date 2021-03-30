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
        expected = 199
        result = add(*self.args)
        print("The result is: ", result)
        # assertEqual = Compare the diffrence between expected and actual result        
        self.assertEqual(expected, result)

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
    accumlate = 0
    basic = 132000

    print("Single Tax Calculation")
    print("\n")
    income = int(input("Input Annual Income: "))
    expected = int(input("Enter the expected result: "))

    # MPF calculation 
    if income > 360000:
        mpf = 18000
    elif income < 360000:  
        mpf = income * 5/100
    print("The MPF allowance is: ", mpf)

    # Standard tax rate calculation
    standard = (income - mpf)*15/100
    print("Standard Rate Tax Total: ", standard)

    # non standard tax rate calculation
    netcharge = income - mpf - basic
    if netcharge < 1:
        accumlate = 0 
    if netcharge < 50000:
        accumlate = netcharge * 0.02
    elif netcharge < 100000:
        accumlate = 50000 * 0.02 + (netcharge - 50000) * 0.06
    elif netcharge < 150000:
        accumlate = 50000 * 0.02 + 50000 * 0.06 + (netcharge - 100000) * 0.1
    elif netcharge < 200000:
        accumlate = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + (netcharge - 150000) * 0.14
    elif netcharge < 250000:
        accumlate = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + 50000 * 0.14 + (netcharge - 200000) * 0.17
    else:
        accumlate = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + 50000 * 0.14 + (netcharge - 200000) * 0.17
    if accumlate <= 0:
        accumlate = 0
    print("Non Standard Rate Tax Total: ", accumlate)
    result = accumlate

    #Recommendation
    if accumlate > standard:
        print("You are recommended to use standard rate")
    else:
        print ("You are recommended to use non-standard rate")
# single ends

    #Testing
    print("")
    print("---------------------------------------------------------")
    print("Run 1 test in 0.002s")
    if expected == result:
        print("OK")
    else:
        print("Failed")
        

def marriage():
    accumlate_A = 0
    accumlate_B = 0
    basic = 132000

    print("Marriage Tax Calculation")
    print("\n")
    income_A = int(input("Input Self Annual Income: "))
    income_B = int(input("Input Spouse Annual Income: "))
    expected = int(input("Enter the expected result: "))

    # A calculation
    # Self MPF calculation 
    if income_A > 360000:
        mpf_A = 18000
    elif income_A < 360000:  
        mpf_A = income_A * 5/100
    print("The Self MPF allowance is: ", mpf_A)

    # Self Standard tax rate calculation
    standard_A = (income_A - mpf_A)*15/100
    print("Self Standard Rate Tax Total: ", standard_A)

    # Self non standard tax rate calculation
    netcharge_A = income_A - mpf_A - basic
    if netcharge_A < 1:
        accumlate_A = 0 
    if netcharge_A < 50000:
        accumlate_A = netcharge_A * 0.02
    elif netcharge_A < 100000:
        accumlate_A = 50000 * 0.02 + (netcharge_A - 50000) * 0.06
    elif netcharge_A < 150000:
        accumlate_A = 50000 * 0.02 + 50000 * 0.06 + (netcharge_A - 100000) * 0.1
    elif netcharge_A < 200000:
        accumlate_A = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + (netcharge_A - 150000) * 0.14
    elif netcharge_A < 250000:
        accumlate_A = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + 50000 * 0.14 + (netcharge_A - 200000) * 0.17
    else:
        accumlate_A = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + 50000 * 0.14 + (netcharge_A - 200000) * 0.17
    if accumlate_A <= 0:
        accumlate_A = 0
    print("Self Non Standard Rate Tax Total: ", accumlate_A)

    # Get lowest Rate
    if accumlate_A > standard_A:
        A_Lowest = standard_A
        print("Self Standard rate is used: $", A_Lowest)
    else:
        A_Lowest = accumlate_A
        print ("Self non-standard rate is used: $", A_Lowest)
    # A ends

    print("--------------------------------------------------")

    # B calculation
    # Self MPF calculation 
    if income_B > 360000:
        mpf_B = 18000
    elif income_B < 360000:  
        mpf_B = income_B * 5/100
    print("The Spouse MPF allowance is: ", mpf_B)

    # Self Standard tax rate calculation
    standard_B = (income_B - mpf_B)*15/100
    print("Spouse Standard Rate Tax Total: ", standard_B)

    # Self non standard tax rate calculation
    netcharge_B = income_B - mpf_B - basic
    if netcharge_B < 1:
        accumlate_B = 0 
    if netcharge_B < 50000:
        accumlate_B = netcharge_B * 0.02
    elif netcharge_B < 100000:
        accumlate_B = 50000 * 0.02 + (netcharge_B - 50000) * 0.06
    elif netcharge_B < 150000:
        accumlate_B = 50000 * 0.02 + 50000 * 0.06 + (netcharge_B - 100000) * 0.1
    elif netcharge_B < 200000:
        accumlate_B = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + (netcharge_B - 150000) * 0.14
    elif netcharge_B < 250000:
        accumlate_B = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + 50000 * 0.14 + (netcharge_B - 200000) * 0.17
    else:
        accumlate_B = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + 50000 * 0.14 + (netcharge_B - 200000) * 0.17
    if accumlate_B <= 0:
        accumlate_B = 0
    print("Spouse Non Standard Rate Tax Total: ", accumlate_B)

    # Get lowest Rate
    if accumlate_B > standard_B:
        B_Lowest = standard_B
        print("Spouse Standard rate is used: $", B_Lowest)
    else:
        B_Lowest = accumlate_B
        print ("Spouse non-standard rate is used: $", B_Lowest)
    # B ends

    print("--------------------------------------------------")

    # Self and spouse lowest tax rate total
    separate_total = A_Lowest + B_Lowest
    print("The total of self and spouse lowest tax rate: $", separate_total)

    print("--------------------------------------------------")
    print("--------------------------------------------------")

    # Joint calculation
    joint_accumlate = 0
    joint_income = income_A + income_B
    joint_mpf = mpf_A + mpf_B
    joint_netcharge = netcharge_A + netcharge_B
    print("The joint income is: $", joint_income)
    print("The joint MPF is: $", joint_mpf)

    if joint_netcharge < 1:
        joint_accumlate = 0 
    if joint_netcharge < 50000:
        joint_accumlate = joint_netcharge * 0.02
    elif joint_netcharge < 100000:
        joint_accumlate = 50000 * 0.02 + (joint_netcharge - 50000) * 0.06
    elif joint_netcharge < 150000:
        joint_accumlate = 50000 * 0.02 + 50000 * 0.06 + (joint_netcharge - 100000) * 0.1
    elif joint_netcharge < 200000:
        joint_accumlate = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + (joint_netcharge - 150000) * 0.14
    elif joint_netcharge < 250000:
        joint_accumlate = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + 50000 * 0.14 + (joint_netcharge - 200000) * 0.17
    else:
        joint_accumlate = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + 50000 * 0.14 + (joint_netcharge - 200000) * 0.17
    if joint_accumlate <= 0:
        joint_accumlate = 0
    print("Joint Non Standard Rate Tax Total: $", joint_accumlate)
    
    joint_standard = (joint_income - joint_mpf) * 0.15
    print("Joint Standard Rate Tax Total: $", joint_standard)

    # Get lowest Rate
    if joint_accumlate > joint_standard:
        joint_Lowest = joint_standard
        print("Self Standard rate is used: $", joint_Lowest)
    else:
        joint_Lowest = joint_accumlate
        print ("Self non-standard rate is used: $", joint_Lowest)

    print("--------------------------------------------------")
    # Get Join and Separate Lowest
    if joint_Lowest > separate_total:
        final_Lowest = separate_total
        print("Separate Taxation should be used: $", final_Lowest)
    else:
        final_Lowest = joint_Lowest
        print ("Joint Assesment should be used: $", final_Lowest)
    result = final_Lowest
    # Joint ends

    #Testing
    print("")
    print("---------------------------------------------------------")
    print("Run 1 test in 0.002s")
    if expected == result:
        print("OK")
    else:
        print("Failed")



def main(argv):
        print("Welcome to Tax Calculator")
        print("-------- Menu -------")
        print("1. Run single tax calulation")
        print("2. Run marriage tax calculation")
        #print("3. run the testing ")
        choice = int(input ("Enter number: "))

        if choice == 1:
            single()

        if choice == 2:
            marriage()

        if choice == 3:
            test()
            

if __name__ == "__main__":
    main(sys.argv)