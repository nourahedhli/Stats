from Calculator.Addition import addition


def Systematic(data):
    List = []

    x = len(data) / 5
    i = 0
    while i < len(data):
        List.append(i)
        i = addition(i, x)
    return List
