import unittest
from calc import Calculator

class CalcTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_adds_two_numbers(self):
        self.calculator.add(1,1)

        self.assertEqual(self.calculator.total, 2)

    @unittest.skip("Needs more work")
    def test_adds_single_number(self):
        calculator = Calculator()

        calculator.add(1)

        self.assertEqual(calculator.total, 1)

    @unittest.expectedFailure
    def test_divide_two_numbers(self):
        calculator = Calculator()

        calculator.divide(1,0)

if __name__ == '__main__':
    unittest.main()
