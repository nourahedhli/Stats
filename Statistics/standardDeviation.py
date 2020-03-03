import numpy as no
from scipy.stats import norm
import math

from Statistics.randomData import random_code
from Statistics.Mean import mean
from Calculator.product import Multiplication
from Calculator.square import square


def StandardDeviationSample(data):
    Sum = 0
    for i in data:
        x = abs(i - mean(data))
        Sum = square(x) + Sum
    n = len(data)
    stand_dev = math.sqrt(Sum / (n - 1))
    return stand_dev


def StandardDeviationPopulation(data):
    Sum1 = 0
    for i in data:
        x = abs(i - mean(data))
        Sum1 = square(x) + Sum1
    n = len(data)
    stand_dev = math.sqrt(Sum1) / n
    return stand_dev
