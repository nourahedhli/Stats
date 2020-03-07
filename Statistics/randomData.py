import random
import pprint
import numpy as np
import decimal


def random_code():
    random.seed(6)
    randomData1 = []
    randomData2 = []
    List = []
    i = 1
    while i < 6:
        y = random.randint(1, 100)
        randomData1.append(y)
        x = '{:04.3f}'.format(random.uniform(1, 100))
        randomData2.append(float(x))
        i += 1
    # select a random item from a list
    randomData1.sort()
    randomData2.sort()

    List = randomData2 + randomData1

    pprint.pprint(List)

    rand_num = random.choice(List)

    # pprint.pprint(rand_num)

    return List


def random_data2():
    random.seed(2)
    i = 0
    list2 = []
    while i < 6:
        x = '{:04.3f}'.format(random.uniform(2, 100))
        list2.append(x)
        i += 1
    pprint.pprint(list2)
    return list2


def random_code_withoutSeed():
    randomData1 = []

    i = 1
    while i < 3:
        y = random.randint(4, 300)
        randomData1.append(y)
        x = "{0:.2f}".format(random.random())
        randomData1.append(x)
        i += 1

    # pprint.pprint(randomData1)
    return randomData1
