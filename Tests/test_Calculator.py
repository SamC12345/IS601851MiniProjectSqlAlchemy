import unittest
import math
from decimal import Decimal
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_mean(self):
        test_data = CsvReader('./Tests/Data/UnitTestAddition.csv').data
        # for row in test_data:
            # nums = [float(val) for val in row['nums'].split('_')]
            # result = float(row['result'])
            # self.assertAlmostEqual(self.calculator.population_mean(nums), result)
            # self.assertAlmostEqual(self.calculator.result, result)
            # self.assertNotEqual(self.calculator.population_mean(nums), result-1)
            # self.assertNotEqual(self.calculator.result, result-1)

if __name__ == '__main__':
    unittest.main()