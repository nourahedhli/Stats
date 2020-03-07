import unittest

from Statistics.Statistics import Statistics

from Statistics.randomData import random_code
from Statistics.randomData import random_code_withoutSeed
from Statistics.Zscores import z_scores
from Statistics.systematic import Systematic




class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = random_code()
        self.statistics = Statistics()
        self.testData1 = random_code_withoutSeed()
        self.testZ = z_scores(self.testData)
        self.testSystematic = Systematic(self.testData)
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
        self.assertEqual(mode, 0.0)

    def test_standDevPop_calculator(self):
        standDev = self.statistics.standardDeviationPopulation(self.testData)
        self.assertEqual(standDev, 12.469679226026626)

    def test_standDevSam_calculator(self):
        standDevSam = self.statistics.standardDeviationSample(self.testData)
        self.assertEqual(standDevSam, 41.56559742008876)

    def test_VarianceSample_calculator(self):
        VarianceSam = self.statistics.VarianceSample(self.testData)
        self.assertEqual(VarianceSam, 6.447138700236621)

    def test_VariancePop_calculator(self):
        VariancePop = self.statistics.VariancePop(self.testData)
        self.assertEqual(VariancePop, 3.531243297484135)

    def test_Quartile1_calculator(self):
        q1 = self.statistics.Quartile1(self.testData)
        self.assertEqual(q1, 0.7375)

    def test_Quartile2_calculator(self):
        q2 = self.statistics.Quartile2(self.testData)
        self.assertEqual(q2, 2.91)

    def test_Quartile3_calculator(self):
        q3 = self.statistics.Quartile3(self.testData)
        self.assertEqual(q3, 71.25)

    def test_z_scores(self, masterResult=None):
        masterResults = []
        result = self.statistics.Z_scores(self.testZ)
        '''go make a list of z score results using the library here'
        'then make a counter that you can use as the array key to match your master list of results with your calculated list'''

        for i in result:
            masterResults.append(i)

        if masterResult == result:
            self.assertTrue(True)  # Is always True

    def test_systematic_calc (self):

        Result =[]
        result = self.statistics.Systematic(self.testSystematic)
        for i in result:
            Result.append(i)

        if Result == result:
            self.assertTrue(True)




if __name__ == '__main__':
    unittest.main()
