import unittest

from math.calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def tearDown(self):
        del self.calculator

    def test_add(self):
        self.assertEqual(self.calculator.add(0, 1), 1)
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertEqual(self.calculator.add(1, -1), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(2, 1), 1)
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertEqual(self.calculator.subtract(1, 2), -1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(0, 1), 0)
        self.assertEqual(self.calculator.multiply(1, 1), 1)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)
        self.assertEqual(self.calculator.multiply(10, 10), 100)

    def test_multiply(self):
        self.assertEqual(self.calculator.divide(0, 1), 0)
        self.assertEqual(self.calculator.divide(1, 1), 1)
        self.assertEqual(self.calculator.divide(-1, 1), -1)
        self.assertEqual(self.calculator.divide(-1, -1), 1)
        self.assertRaises(ValueError, self.calculator.divide, 1, 0)

if __name__ == '__main__':
    unittest.main()
