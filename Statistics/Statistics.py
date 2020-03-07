from Calculator.Calculator import Calculator

from Statistics.Mean import mean
from Statistics.Median import Median
from Statistics.Mode import mode
from Statistics.randomData import random_code
from Statistics.systematic import Systematic
from Statistics.standardDeviation import StandardDeviationPopulation
from Statistics.standardDeviation import StandardDeviationSample
from Statistics.Quartiles import *
from Statistics.marginError import MarginError
from Statistics.Variance import *

from Statistics.Zscores import *
from Statistics.Correlation import *
from Statistics.confidence_interval import *
from Statistics.sampleSize import *
from Statistics.skewness import *
from Statistics.AbsMeanStd import *


class Statistics(Calculator):
    data = []

    def mean(self, data):
        self.result = mean(data)

        return self.result

    def median(self, data):
        self.result = Median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def standardDeviationPopulation(self, data):
        self.result = StandardDeviationPopulation(data)
        return self.result

    def standardDeviationSample(self, data):
        self.result = StandardDeviationSample(data)
        return self.result

    def VariancePop(self, data):
        self.result = population_variance(data)
        return self.result

    def VarianceSample(self, data):
        self.result = sample_variance(data)
        return self.result

    def Quartile1(self, data):
        self.result = quart1(data)
        return self.result

    def Quartile2(self, data):
        self.result = quart2(data)
        return self.result

    def Quartile3(self, data):
        self.result = quart3(data)
        return self.result

    def Z_values(self, data):
        self.result = z_values(data)
        return self.result

    def Systematic(self, data):
        self.result = Systematic(data)
        return self.result

    def Z_scores(self, data):
        self.result = Z_scores(self.Z_values(data))
        return self.result

    def Confidence_interval(self, data):
        self.result = mean_confidence_interval(data)
        return self.result

    def Skewness(self, data):
        self.result = Skewness(data)
        return self.result

    def MarginError(self, data):
        self.result = MarginError(z_values(data))
        return self.result

    def SampleSizeWithoutStd(self, data):
        self.result = SampleSize_withoutStd(data)
        return self.result

    def SampleSizeWithStd(self, data):
        self.result = SampleSize_withStd(data)
        return self.result

    def SampleSizeCochran(self, data):
        self.result = CochranSampleSize(data)
        return self.result

    def MeanAbsStd(self, data):
        self.result = meanAbsDev(data)
        return self.result

    def MeanStd(self, data):
        self.result = meanDev(data)
        return self.result

    def Sample_Correlation(self, list1, list2):
        self.result = Sample_Correlation(list1, list2)
        return self.result

    def Population_Correlation(self, list1, list2):
        self.result = Population_Correlation(list1, list2)
        return self.result
