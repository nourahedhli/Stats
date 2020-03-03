import unittest

from Statistics.Statistics import Statistics

from Statistics.randomData import random_code
from Statistics.randomData import random_code_withoutSeed


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = random_code()
        self.statistics = Statistics()
        self.testData1 = random_code_withoutSeed()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 32.79)

    def test_median_calculator(self):
        median = self.statistics.median(self.testData)
        self.assertEqual(median, 2.91)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, 1)

    def test_standDev_calculator(self):
        standDev = self.statistics.standardDeviation(self.testData)
        self.assertEqual(standDev, 21.736666666666668)


if __name__ == '__main__':
    unittest.main()
