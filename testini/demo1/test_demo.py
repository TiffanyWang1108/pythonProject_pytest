"""
Name : test_demo.py
Author  : Tiffany
Time : 2022/6/17 17:12
DESC: 
"""
import logging


class TestDemo:
    def test_case1(self):
        logging.info('This is the first testcase')
        assert 1 == 1

    def test_case2(self):
        assert 2 == 2
