# https://github.com/ebisher/lab10-EB-FA.git
# Partner 1: Ella Bisher
# Partner 2: Frank Ascencio

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-2, 3), -5)
        self.assertEqual(subtract(1, -1), 2)
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(3, 10), 10 / 3)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        pass

    def test_logarithm(self): # 3 assertions
        self.assertTrue(logarithm(10, 100), 2)
        self.assertTrue(logarithm(2, 8), 3)
        self.assertTrue(logarithm(5, 25), 2)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(1, 0)
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):  # base <= 0
            logarithm(0, 10)
        with self.assertRaises(ValueError):  # base == 1
            logarithm(1, 10)
        with self.assertRaises(ValueError):  # argument <= 0
            logarithm(10, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)


    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-9)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()