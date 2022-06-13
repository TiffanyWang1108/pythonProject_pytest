"""
Name : test_skipif.py
Author  : Tiffany
Time : 2022/6/13 22:12
DESC: 
"""
import pytest
import sys

print(sys.platform)


@pytest.mark.skipif(sys.platform == "win", reason="dose not run on windows")
def test_case1():
    assert True


@pytest.mark.skipif(sys.version_info < (3, 12), reason="need higher python version")
def test_case2():
    assert True
