import unittest
import math
from Statistics.Statistics import Statistics as statistic
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistic = statistic()

    def test_Add(self):
        test_data = CsvReader('./Tests/Data/Unit\ Test\ Addition.csv').data
        for row in test_data:
            a= int(row['Value 1'])
            b= int(row['Value 2'])
            result = float(row['Result'])
            self.assertEqual(self.statistic.add(a,b), result)
            self.assertNotEqual(self.statistic.add(a,b), result-1)

    
if __name__ == '__main__':
    unittest.main()
    