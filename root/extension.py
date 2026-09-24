
import pytest

def double_integer(a: int) -> int:
    """Double an integer.

    :param a: The value to double.
    :return: The doubled value.
    """
    double = a * 2
    return double


def add(a: float, b: float) -> float:
    """Adds two numbers together

    :param a: First number to add.
    :param b: Second number to add.
    :return: Sum of two numbers.
    """
    total = a + b
    return total

def divide(a: float, b: float):
    #this will the divide two numbers listed.
    half = a / 4
    return half
# prints the value that we got from the function

def test_double_integer():
    assert double_integer(2) == 4

def test_double_integer_two():
    assert double_integer(6) == 12

def test_add():
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_add_two():
    assert add(0.5, 0.6) == pytest.approx(1.1)

def test_divide():
    assert divide(12, 4) == 3

def test_divide():
    assert divide(16, 4) == 4


