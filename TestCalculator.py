import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    ############################Addition Tests##########################
    def test_add_positive(self):
        self.assertEqual(self.calc.add(3, 3), 5)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_add_mixed(self):
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_add_float(self):
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)


    ###########################Subtraction Tests##########################
    def test_subtraction_positive(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtraction_negative(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtraction_mixed(self):
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    def test_subtraction_float(self):
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)
        

    ############################Multiplication Tests##########################
    def test_multiplication_positive(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
    
    def test_multiplication_negative(self):
        self.assertEqual(self.calc.multiply(-2, -5), 10)

    def test_multiplication_mixed(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_multiplication_float(self):
        self.assertEqual(self.calc.multiply(-3.2, -4), 12.8)

    def test_multiplication_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    ##########################Division Tests##########################
    def test_division_positive(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_mixed(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
    
    def test_division_float(self):
        self.assertEqual(self.calc.divide(5.5, 2), 2.75)

    def test_division_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
        
if __name__ == '__main__':
    unittest.main()