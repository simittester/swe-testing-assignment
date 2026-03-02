import pytest
from quick_calc.core import Calculator


def test_addition_basic():
    c = Calculator()
    assert c.add(5, 3) == 8


def test_subtraction_basic():
    c = Calculator()
    assert c.sub(10, 4) == 6


def test_multiplication_basic():
    c = Calculator()
    assert c.mul(6, 7) == 42


def test_division_basic():
    c = Calculator()
    assert c.div(20, 5) == 4


def test_division_by_zero():
    c = Calculator()
    with pytest.raises(ZeroDivisionError):
        c.div(5, 0)


def test_negative_numbers():
    c = Calculator()
    assert c.add(-2, -3) == -5


def test_decimal_numbers():
    c = Calculator()
    assert c.div(1, 4) == 0.25


def test_large_numbers():
    c = Calculator()
    assert c.mul(10**9, 3) == 3 * 10**9