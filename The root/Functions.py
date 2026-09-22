import pytest


def double_integer(a):
    double = a * 2
    return double


def add(a, b):
    total = a + b
    return total


def subtract(a, b):
    difference = a - b
    return difference


def test_pass():
    assert 1 == 1


def test_fail():
    assert True


def test_double_integer():
    assert 4 == double_integer(2)


def test_double_integer_negative():
    assert -10 == double_integer(-5)


def test_add():
    assert pytest.approx(0.3) == add(0.1, 0.2)


def test_add_whole_numbers():
    assert 10 == add(4, 6)


def test_subtract():
    assert 5 == subtract(10, 5)


def test_subtract_negative():
    assert -3 == subtract(2, 5)