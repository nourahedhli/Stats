import random
import pprint

import decimal


def random_code():
    random.seed(3)
    randomData = []
    i = 1
    while i < 6:
        randomData.append(random.randint(1, 100))
        x = "{0:.2f}".format(random.random())
        randomData.append(x)
        i += 1
    pprint.pprint(randomData)
    return randomData


def random_code_withoutSeed():
    randomData1 = []
    i = 1
    while i < 3:
        randomData1.append(random.randint(4, 300))
        x = "{0:.2f}".format(random.random())
        randomData1.append(x)
        i += 1

    pprint.pprint(randomData1)
    return randomData1
