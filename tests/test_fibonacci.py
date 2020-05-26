import unittest

from math.fibonacci import Fibonacci

class FibonacciTest(unittest.TestCase):
    def setUp(self):
        self.bibonacci = Fibonacci()

    def tearDown(self):
        del self.bibonacci

    def test_calculate_negative(self):
        self.assertRaises(ValueError, self.bibonacci.calculate, -1)

    def test_calculate_zero(self):
        self.assertEqual(self.bibonacci.calculate(0), 0)

    def test_calculate_one(self):
        self.assertEqual(self.bibonacci.calculate(1), 1)

    def test_calculate_two(self):
        self.assertEqual(self.bibonacci.calculate(2), 1)

    def test_calculate_three(self):
        self.assertEqual(self.bibonacci.calculate(3), 2)

    def test_calculate_larger(self):
        self.assertEqual(self.bibonacci.calculate(10), 55)
        self.assertEqual(self.bibonacci.calculate(20), 6765)

if __name__ == '__main__':
    unittest.main()
