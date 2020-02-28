from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.randomData import random_code


def Median(data):
    n = len(data)
    num = n // 2
    if n % 2 == 0:
        mid = (data[num] + data[num - 1]) / 2
        print(data[num])
    else:
        mid = data[num]
        print(data[mid])
    return mid
