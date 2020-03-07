from Statistics.Zscores import *
from Statistics.standardDeviation import StandardDeviationSample
from Calculator.squareRoot import squareRoot


def MarginError(data):
    List = []
    SE = (StandardDeviationSample(data) / (squareRoot(len(data))))
    for i in Z_scores(z_values(data)):
        ME = i * SE
        List.append(ME)

    return List
