from scipy.stats import skew


def Skewness(data):
    result = skew(data)
    return result
