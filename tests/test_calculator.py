# tests/test_calculator.py

import unittest
from simple_calculator.simple_calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 6)
        self.assertEqual(result, 24)

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(8, 4)
        self.assertEqual(result, 2)

        with self.assertRaises(ValueError):
            calc.divide(5, 0)
