import pytest
from calculator import add, subtract, multiply, power, divide


def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-4, -6) == -10

def test_add_mixed_sign():
    assert add(-1, 5) == 4


def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6

def test_subtract_negative_numbers():
    assert subtract(-3, -2) == -1

def test_subtract_resulting_in_negative():
    assert subtract(2, 9) == -7


def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(7, 0) == 0

def test_multiply_negative_numbers():
    assert multiply(-2, -5) == 10


def test_power_positive_exponent():
    assert power(2, 10) == 1024

def test_power_zero_exponent():
    assert power(5, 0) == 1

def test_power_negative_exponent():
    assert power(2, -1) == 0.5


def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0

def test_divide_resulting_in_float():
    assert divide(7, 2) == 3.5

def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
