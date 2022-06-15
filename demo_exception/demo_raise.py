"""
Name : demo_raise.py
Author  : Tiffany
Time : 2022/6/14 16:11
DESC: 
"""
import pytest


def test_raise():
    with pytest.raises((ValueError, ZeroDivisionError)):
        raise ZeroDivisionError('除数为0')


def test_raise1():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 42")
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "value must be 42"




