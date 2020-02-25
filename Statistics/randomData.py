import random
import pprint


def random_code():
    random.seed(3)
    randomData = []
    i = 1
    while i < 6:
        randomData.append(random.randint(1, 100))
        i += 1
        pprint.pprint(randomData)
    return randomData
