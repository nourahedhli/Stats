from Statistics.Zscores import *
from Statistics.standardDeviation import StandardDeviationSample
from Calculator.squareRoot import squareRoot


def MarginError(data):

    List = []
    SE = int(StandardDeviationSample(data) / (squareRoot(len(data))))
    for i in zscore(z_values(data)):
        ME = i * SE
        List.append(ME)

    return List
