from Calculator.Calculator import Calculator

from Statistics.Mean import mean

from Statistics.randomData import random_code


class Statistics(Calculator):
    data = []

    def mean(self, data):
        self.result = mean(data)

        return self.result
