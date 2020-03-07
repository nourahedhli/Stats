
from statistics import mean
from Statistics.standardDeviation import StandardDeviationSample
from Statistics.Zscores import Z_scores


from Statistics.Zscores import z_values


def mean_confidence_interval(data):
    n = len(data)
    List = []
    std = StandardDeviationSample(data)
    mu = mean(data)
    z_list = Z_scores(z_values(data))
    SE = std / n
    for i in z_list:
        left = mu - i * SE
        right = mu + i * SE
        List.append([left, right])
    return List
