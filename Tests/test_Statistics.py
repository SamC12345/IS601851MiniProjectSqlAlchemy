import unittest
import math
from Statistics.Statistics import Statistics as statistic
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistic = statistic()

    def test_Add(self):
        test_data = CsvReader('./Tests/Data/UnitTestAddition.csv').data
        for row in test_data:
            a= int(row['Value 1'])
            b= int(row['Value 2'])
            result = int(row['Result'])
            self.assertEqual(self.statistic.add(a,b), result)
            self.assertNotEqual(self.statistic.add(a,b), result-1)

    def test_Subtract(self):
        test_data = CsvReader('./Tests/Data/UnitTestSubtraction.csv').data
        for row in test_data:
            a= int(row['Value 1'])
            b= int(row['Value 2'])
            result = int(row['Result'])
            self.assertEqual(self.statistic.subtract(a,b), result)
            self.assertNotEqual(self.statistic.subtract(a,b), result-1)
    def test_Multiply(self):
        test_data = CsvReader('./Tests/Data/UnitTestMultiplication.csv').data
        for row in test_data:
            a= int(row['Value 1'])
            b= int(row['Value 2'])
            result = int(row['Result'])
            self.assertEqual(self.statistic.multiply(a,b), result)
            self.assertNotEqual(self.statistic.multiply(a,b), result-1)
    
    def test_Divide(self):
        test_data = CsvReader('./Tests/Data/UnitTestDivision.csv').data
        for row in test_data:
            a= int(row['Value 1'])
            b= int(row['Value 2'])
            result = float(row['Result'])
            self.assertAlmostEqual(self.statistic.divide(a,b), result)
            self.assertNotEqual(self.statistic.divide(a,b), result-1)

    def test_Square(self):
        test_data = CsvReader('./Tests/Data/UnitTestSquare.csv').data
        for row in test_data:
            a= int(row['Value 1'])
            result = int(row['Result'])
            self.assertEqual(self.statistic.square(a), result)
            self.assertNotEqual(self.statistic.square(a), result-1)

    def test_SquareRoot(self):
        test_data = CsvReader('./Tests/Data/UnitTestSquareRoot.csv').data
        for row in test_data:
            a= int(row['Value 1'])
            result = float(row['Result'])
            self.assertAlmostEqual(self.statistic.squareRoot(a), result)
            self.assertNotEqual(self.statistic.squareRoot(a), result-1)
    
if __name__ == '__main__':
    unittest.main()
    