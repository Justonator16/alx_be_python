import unittest
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)

    def test_subtractation(self):
        self.assertEqual(self.calc.subtract(5,3),2)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,3),6)

    def test_division(self):
        self.assertEqual(self.calc.divide(4,0),None)
        self.assertEqual(self.calc.divide(4,2),2)