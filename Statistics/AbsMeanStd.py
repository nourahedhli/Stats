from numpy import mean, absolute


def meanAbsDev(data):
    m_a_d = mean(absolute(data - mean(data)))
    return m_a_d
