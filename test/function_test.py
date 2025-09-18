from src.function import add_numbers


def test_add_number_simple():
    """add_number() should work with positive integers"""
    assert add_numbers(10, 10) == 20


def test_add_number_negative():
    """add_number() should work with negative integers"""
    assert add_numbers(-10, 10) == 0


def test_add_number_both_negative():
    """add_number() should work with zero"""
    assert add_numbers(10, 0) == 10
