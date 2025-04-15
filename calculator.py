# https://github.com/ebisher/lab10-EB-FA.git
# Partner 1: Ella Bisher
# Partner 2: Frank Ascencio

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithm base must be > 0 and ≠ 1, and argument must be > 0.")
    return math.log(b, a)

def exp(a, b):
    return a ** b