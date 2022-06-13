"""
Name : test_params2.py
Author  : Tiffany
Time : 2022/6/13 18:39
DESC: 
"""

import pytest


@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("4+5", 9), ("3+6", 9)], ids=["1", '2', 3])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected
