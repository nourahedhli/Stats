from Statistics.marginError import MarginError
from Statistics.confidence_interval import mean_confidence_interval
from Calculator.product import product
from Calculator.square import square
import scipy
from scipy import stats
from Statistics.standardDeviation import StandardDeviationSample
from Calculator.Division import division
from Statistics.Zscores import *


def SampleSize_withoutStd(data):
    E = MarginError(data)  # return a list
    p = 0.5
    q = 1 - p
    PQ = product(q, p)
    List = []
    List1 = []
    x = mean_confidence_interval(data)
    for i in x:
        Z = i[1] / 2
        List.append(scipy.stats.norm.cdf(Z))
    ME = []
    for i in E:
        ME.append(i / 2)
    i = 0
    while i < len(ME):
        ZE = List[i] / ME[i]
        x = round(square(ZE) * PQ)
        List1.append(x)
        i += 1
    return List1


def SampleSize_withStd(data):
    List = []
    List1 = []
    E = MarginError(data)
    K = mean_confidence_interval(data)
    for i in K:
        Z = i[1] / 2
        List.append(scipy.stats.norm.cdf(Z))
    i = 0
    while i < len(List):
        x = product(List[i], StandardDeviationSample(data))
        y = round(division(x, E[i]))
        List1.append(square(y))
        i += 1
    return List1


def CochranSampleSize(data):

    p = 0.5
    q = 1 - p
    PQ = product(p, q)
    List = []
    List1 = []
    for i in MarginError(data):
        List.append(square(i))

    for i in Z_scores(z_values(data)):
        List1.append(square(i))
    i = 0
    n = []
    while i < len(List):
        n.append(product(List[i], PQ) / List1[i])
        i += 1
    return n