"""
Name : test_command.py
Author  : Tiffany
Time : 2022/6/14 12:05
DESC: 
"""


def double(a):
    return a * 2


def test_double_int():
    assert 2 == double(1)


def test_double1_minus():
    assert -20 == double(-1)


def test_double_float():
    assert 0.2 == double(0.1)


def test_double2_minus():
    assert -0.2 == double(-0.1)


def test_double_0():
    assert 0 == double(0)


def test_double_bignum():
    assert 200 == double(100)


def test_double_str():
    assert 'aa' == double('a')


def test_double_str1():
    assert 'a$a$' == double('a$')

