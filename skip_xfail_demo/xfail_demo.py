"""
Name : xfail_demo.py
Author  : Tiffany
Time : 2022/6/13 22:19
DESC: 
"""
import pytest


def test_xfail():
    print("开始测试")
    pytest.xfail(reason="该功能未完成")
    print("测试步骤")
    assert True


@pytest.mark.xfail
def test_a():
    print("test_xfail")
    assert 1 == 2


xfail = pytest.mark.xfail


@xfail(reason="bug 001")
def test_b():
    assert 0
