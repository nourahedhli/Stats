from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.randomData import random_code


def mode(data):
    d = {}
    for num in data:
        if num not in d.keys():
            d[num] = 1
        else:
            d[num] += 1

    Mode = max(d.values())
    print(Mode)
    return Mode
