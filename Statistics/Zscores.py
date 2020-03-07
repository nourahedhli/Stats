from scipy import stats

from statistics import mean
from Statistics.Variance import population_variance
import scipy


def z_values(data):
    list1 = []
    for i in data:
        Z = (i - mean(data)) / (population_variance(data))
        list1.append(Z)
    return list1


def Z_scores(list1):
    valueList = []
    for i in list1:
        valueList.append(scipy.stats.norm.cdf(i))
    return valueList
