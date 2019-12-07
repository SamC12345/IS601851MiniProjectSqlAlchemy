import unittest
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('./Tests/Data/UnitTestAddition.csv')

    def test_get_data(self):
        self.assertGreaterEqual(len(self.csv_reader.data),1)

if __name__ == '__main__':
    unittest.main()
