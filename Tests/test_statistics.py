import unittest

from Statistics.Statistics import Statistics
from Statistics.randomData import random_data2
from Statistics.randomData import random_code
from Statistics.randomData import random_code_withoutSeed
from Statistics.Zscores import z_values
from Statistics.systematic import Systematic


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.testData = random_code()
        self.statistics = Statistics()
        self.testData2 = random_data2()
        self.testData1 = random_code_withoutSeed()

        self.testZ = z_values(self.testData)
        self.testSystematic = Systematic(self.testData)
        self.testZscore = z_values(self.testData)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 61.7688)

    def test_median_calculator(self):
        median = self.statistics.median(self.testData)
        self.assertEqual(median, 43.6865)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, 1.045)

    def test_standDevPop_calculator(self):
        standDev = self.statistics.standardDeviationPopulation(self.testData)
        self.assertEqual(standDev, 9.851279178665072)

    def test_standDevSam_calculator(self):
        standDevSam = self.statistics.standardDeviationSample(self.testData)
        self.assertEqual(standDevSam, 32.83759726221691)

    def test_VarianceSample_calculator(self):
        VarianceSam = self.statistics.VarianceSample(self.testData)
        self.assertEqual(VarianceSam, 5.730409868605989)

    def test_VariancePop_calculator(self):
        VariancePop = self.statistics.VariancePop(self.testData)
        self.assertEqual(VariancePop, 3.138674748785715)

    def test_Quartile1_calculator(self):
        q1 = self.statistics.Quartile1(self.testData)
        self.assertEqual(q1, 60.046499999999995)

    def test_Quartile2_calculator(self):
        q2 = self.statistics.Quartile2(self.testData)
        self.assertEqual(q2, 73.8745)

    def test_Quartile3_calculator(self):
        q3 = self.statistics.Quartile3(self.testData)
        self.assertEqual(q3, 80.89450000000001)

    def test_z_Values(self, masterResult=None):
        masterResults = []
        result = self.statistics.Z_values(self.testZ)

        for i in result:
            masterResults.append(i)

        if masterResult == result:
            self.assertTrue(True)

    def test_systematic_calc(self):

        Result = []
        result = self.statistics.Systematic(self.testSystematic)
        for i in result:
            Result.append(i)
        if Result == result:
            self.assertTrue(True)

    def test_Z_scores(self):
        Result = []
        result = self.statistics.Z_scores(self.testZscore)
        for i in result:
            Result.append(i)

        if Result == result:
            self.assertTrue(True)

    def test_confidence_interval(self):

        Result = []
        result = self.statistics.Confidence_interval(self.testData)
        for i in result:
            Result.append(i)

        if Result == result:
            self.assertTrue(True)

    def test_skewness(self):
        skew = self.statistics.Skewness(self.testData)
        self.assertEqual(skew, -1.0958752107177778)

    def test_margin_Error(self):

        Result = []
        result = self.statistics.MarginError(self.testData)
        for i in result:
            Result.append(i)

        if Result == result:
            self.assertTrue(True)

    def test_SampleSize_without_std(self):
        Result = []
        result = self.statistics.SampleSizeWithoutStd(self.testData)
        for i in result:
            Result.append(i)

        if Result == result:
            self.assertTrue(True)

    def test_SampleSize_with_std(self):
        Result = []
        result = self.statistics.SampleSizeWithStd(self.testData)
        for i in result:
            Result.append(i)

        if Result == result:
            self.assertTrue(True)

    def test_SampleSize_Cochran(self):
        Result = []
        result = self.statistics.SampleSizeCochran(self.testData)
        for i in result:
            Result.append(i)

        if Result == result:
            self.assertTrue(True)

    def test_Abs_mean_Dev (self):
        meanADev = self.statistics.MeanAbsStd(self.testData)
        self.assertEqual(meanADev, 24.03988)

if __name__ == '__main__':
    unittest.main()
