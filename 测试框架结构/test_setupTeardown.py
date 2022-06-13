"""
Name : test_setupTeardown.py
Author  : Tiffany
Time : 2022/6/13 14:01
DESC: 
"""


# 模块级别，只被调用一次
def setup_module():
    print("资源准备：setup module")


def teardown_module():
    print("资源销毁：teardown module")


def test_case1():
    print("case1")


def test_case2():
    print("case2")


def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源销毁：teardown function")
