from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.randomData import random_code
from Statistics.standardDeviation import StandardDeviationPopulation
from Statistics.standardDeviation import StandardDeviationSample
from Calculator.square import square


def population_variance(data):
    x = StandardDeviationPopulation(data)
    return square(x)


def sample_variance(data):
    x = StandardDeviationSample(data)
    return square(x)
