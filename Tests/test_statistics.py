import unittest
import random
from Statistics.Statistics import Statistics
import pprint
import numpy
from Statistics.randomData import randomcode


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:

        self.testData = randomcode()
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 48.0)


if __name__ == '__main__':
    unittest.main()
