"""
Name : test_skip.py
Author  : Tiffany
Time : 2022/6/13 19:06
DESC: 
"""

import pytest


@pytest.mark.skip
def test_aa():
    assert True


@pytest.mark.skip(reason="代码还未实现")
def test_bbb():
    assert False


# 代码中添加 跳过代码块：pytest.skip(reason="")
def check_login():
    return True


def test_function():
    print('start')
    # 如果未登录，则跳过后续步骤
    if not check_login():
        pytest.skip("unsupported configuration")
    print('end')







