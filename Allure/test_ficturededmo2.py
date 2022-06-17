"""
Name : test_ficturededmo2.py
Author  : Tiffany
Time : 2022/6/17 14:12
DESC: 
"""
#  fixture的作用域

import pytest

@pytest.fixture(scope="module")
def login():
    print("完成登录操作")


def test_search():
    print("搜索")


def test_cart(login):
    print("购物车")


def test_order(login):
    print("下单功能")