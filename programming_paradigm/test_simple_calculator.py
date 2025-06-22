# Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator class 
# that supports addition, subtraction, multiplication, and division operations.

# Task: Write Unit Tests in test_simple_calculator.py
# Create a test_simple_calculator.py script to define and run unit tests for each method in the SimpleCalculator class. 
# Your tests should cover various scenarios to ensure the class functions correctly.

# Guidelines for Writing Tests:
# Import the Necessary Modules:

# Import the unittest module and the SimpleCalculator class from simple_calculator.py.
# Define a Test Class:

# Create a test class that inherits from unittest.TestCase.
# Write Test Methods:

# Write at least one test method for each operation (add, subtract, multiply, divide) provided by the SimpleCalculator.
# Include tests for edge cases, such as dividing by zero.
# Use Assertions to Verify Results:

# Utilize self.assertEqual() to check for expected outcomes.
# For the divide method, ensure you test both normal operation and division by zero.
# Running Your Tests:

# Run your tests using the command line: python -m unittest test_simple_calculator.py.

# Note for you:
# Your goal is to think like a tester and identify as many relevant test cases as possible for each method.
# Pay special attention to potential edge cases, such as division by zero, which could lead to 
# unexpected behaviors if not properly handled.
# Writing comprehensive tests not only helps ensure your code is working 
# correctly but also improves your understanding of how the code operates under different conditions.


import unittest 
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,4), 6)
        self.assertEqual(self.calc.add(-2,2), 0)
        self.assertEqual(self.calc.add(4,0), 4)
        self.assertEqual(self.calc.add(8,-2), 6)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2,-3), 5)
        self.assertEqual(self.calc.subtract(8,4), 4)
        self.assertEqual(self.calc.subtract(0,4), -4)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(7,5), 35)
        self.assertEqual(self.calc.multiply(0,9), 0)
        self.assertEqual(self.calc.multiply(6,1), 6)
        self.assertEqual(self.calc.multiply(-4,-3), 12)

    def test_division(self):
        self.assertEqual(self.calc.divide(8,2), 4)
        self.assertEqual(self.calc.divide(0,3), 0)
        self.assertEqual(self.calc.divide(9,9), 1)
        self.assertEqual(self.calc.divide(5,0), None)
        self.assertEqual(self.calc.divide(7,2), 3.5)

if __name__ == "__main__":
    unittest.main()