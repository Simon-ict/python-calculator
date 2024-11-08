import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
# ------------------------------------------------------------------
    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
# ------------------------------------------------------------------
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
# ------------------------------------------------------------------
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 1), 1)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 1), 1)
# ------------------------------------------------------------------
    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 1), 1)
    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 1), 1)
# ------------------------------------------------------------------
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(2, 1), 1)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(2, 1), 1)
# ------------------------------------------------------------------        
if __name__ == '__main__':
    unittest.main()