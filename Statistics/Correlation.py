from Calculator.squareRoot import squareRoot
from Calculator.square import square

from Calculator.product import product
from Calculator.Subtraction import subtraction


def average(x):
    summation = sum(x)
    return float(summation) / len(x)


def Population_Correlation(list1, list2):
    avg_x = average(list1)
    avg_y = average(list2)
    n = len(list1)

    y2 = 0
    x2 = 0
    rod = 0
    for i in range(n):
        x = subtraction(list1[i], avg_x)
        y = subtraction(list2[i], avg_y)
        rod += product(x, y)
        x2 += square(x)
        y2 += square(y)

    return rod / squareRoot(x2 * y2)


def Sample_Correlation(list1, list2):
    n = len(list1)

    avg_x = average(list1)
    avg_y = average(list2)
    rod = 0
    x2 = 0
    y2 = 0
    for i in range(n):
        x = subtraction(list1[i], avg_x)
        y = subtraction(list2[i], avg_y)
        rod += product(x, y)
        x2 += square(x)
        y2 += square(y)

    return rod / squareRoot(x2 * y2)
