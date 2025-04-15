import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        pass

    def test_subtract(self): # 3 assertions
        pass
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(2, 10), 5)
        self.assertAlmostEqual(divide(3, 10), 10 / 3)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        pass

    def test_logarithm(self): # 3 assertions
        pass

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        pass
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