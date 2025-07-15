import pytest
from is_even import is_even


def test_even_numbers():
    """Test that even numbers return True"""
    assert is_even(0) == True
    assert is_even(2) == True
    assert is_even(4) == True
    assert is_even(-2) == True
    assert is_even(100) == True


def test_odd_numbers():
    """Test that odd numbers return False"""
    assert is_even(1) == False
    assert is_even(3) == False
    assert is_even(5) == False
    assert is_even(-1) == False
    assert is_even(99) == False


def test_zero():
    """Test that zero is considered even"""
    assert is_even(0) == True


def test_negative_numbers():
    """Test both positive and negative numbers"""
    assert is_even(-4) == True
    assert is_even(-3) == False
    assert is_even(-10) == True
    assert is_even(-7) == False
