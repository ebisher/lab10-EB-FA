"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)
    except ValueError as ve:
        raise ve

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        raise e

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be greater than 0 and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be greater than 0.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b