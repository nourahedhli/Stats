import random
import pprint


def randomcode():
    random.seed(9)
    randomData = []
    i = 1
    while i < 6:
        randomData.append(random.randint(1, 100))
        i += 1
        pprint.pprint(randomData)
