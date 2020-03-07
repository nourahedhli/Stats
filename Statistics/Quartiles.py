from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.randomData import random_code

from Calculator.squareRoot import squareRoot
import math
import numpy as np


def quart1(data):
    q1 = np.quantile(data, 0.25)
    return q1


def quart2(data):
    q2 = np.quantile(data, 0.50)
    return q2


def quart3(data):
    q3 = np.quantile(data, 0.75)
    return q3
