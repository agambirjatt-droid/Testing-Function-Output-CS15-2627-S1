import pytest


def double_integer(a):
    double = a * 2
    return double


def add(a, b):
    total = a + b
    return total


def test_pass():
    assert 1 == 1


def test_fail():
    assert True


def test_double_integer():
    assert 4 == double_integer(2)


def test_add():
    assert pytest.approx(0.3) == add(0.1, 0.2)