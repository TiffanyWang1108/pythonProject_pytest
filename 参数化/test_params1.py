"""
Name : test_params1.py
Author  : Tiffany
Time : 2022/6/13 18:29
DESC: 
"""

import pytest

search_list = ['appium', 'selenium', 'pytest']  # 列表 or 元组


@pytest.mark.parametrize('name', search_list)
def test_search(name):
    assert name in search_list
