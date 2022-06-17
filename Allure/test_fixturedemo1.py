"""
Name : test_fixturedemo1.py
Author  : Tiffany
Time : 2022/6/17 13:56
DESC: 
"""
import pytest

@pytest.fixture()
def login():
    print("完成登录操作")


def test_search():
    print("搜索")


def test_cart(login):
    print("购物车")


def test_order(login):
    print("下单功能")


