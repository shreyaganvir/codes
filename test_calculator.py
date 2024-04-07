import unittest
from calculator import Calculator  # Assuming Calculator class is defined in calculator.py

class TestCalculator(unittest.TestCase):

    def setUp(self):
        print("Initialize Calculator")
        self.calc = Calculator()

    def test_subtraction(self):
        print("Test substract")
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_division(self):
        print("Test divide")
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_multiplication(self):
        print("Test multiply")
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_addition(self):
        print("Test add")
        result = self.calc.add(5, 10)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()