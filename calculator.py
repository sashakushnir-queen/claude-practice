import math


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the result of subtracting b from a."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


def divide(a, b):
    """Return the result of dividing a by b, raising ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def square_root(a):
    """Return the square root of a, raising ValueError if a is negative."""
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)
