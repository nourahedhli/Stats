from Calculator.Calculator import Calculator

from Statistics.Mean import mean
from Statistics.Median import Median
from Statistics.Mode import mode
from Statistics.randomData import random_code


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
