from Calculator.Files.Addition import addition
from Calculator.Files.Subtraction import subtraction
from Calculator.Files.Multiplication import multiplication
from Calculator.Files.Division import division
from Calculator.Files.Square import squaring
from Calculator.Files.SquareRoot import square_rooting

class Calculator:

    def __init__(self):
        pass

    def add(self,a,b):
        return addition(a,b)

    def subtract(self,a,b):
        return subtraction(a,b)
    def multiply(self,a,b):
        return multiplication(a,b)
    def divide(self,a,b):
        return division(a,b)
    def square(self,a):
        return squaring(a)
    def square_root(self,a):
        return square_rooting(a)