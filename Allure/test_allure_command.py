"""
Name : test_allure_command.py
Author  : Tiffany
Time : 2022/6/17 13:17
DESC: 
"""


import pytest


def test_success():
    """
    this test succeed
    :return:
    """
    assert True


def test_failure():
    """this test fail"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops!')
