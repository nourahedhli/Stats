import unittest
import random
from Statistics.Statistics import Statistics
import pprint
import numpy as np
from Statistics.randomData import random_code


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:

        self.testData = random_code()
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 48.4)


if __name__ == '__main__':
    unittest.main()
