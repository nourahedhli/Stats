from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.square import square
from Calculator.squareRoot import squareRoot
from Calculator.Division import division
from Calculator.product import product


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def SquareRoot(self, a):
        self.result = squareRoot(a)
        return self.result

    def Division(self, a, b):
        self.result = division(a, b)
        return self.result

    def Product(self, a, b):
        self.result = product(a, b)
        return self.result
