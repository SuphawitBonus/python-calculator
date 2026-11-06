import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    # add() - 2 test cases
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(5, 0), 5)

    # subtract() - 2 test cases
    def test_subtract_basic(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    # multiply() - 2 test cases
    def test_multiply_basic(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(4, 0), 0)

    # divide() - 2 test cases
    def test_divide_exact(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_divide_with_remainder(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    # modulo() - 2 test cases
    def test_modulo_with_remainder(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modulo_exact(self):
        self.assertEqual(self.calc.modulo(6, 3), 0)

if __name__ == '__main__':
    unittest.main()
