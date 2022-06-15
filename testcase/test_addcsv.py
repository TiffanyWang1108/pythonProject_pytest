"""
Name : test_addcsv.py
Author  : Tiffany
Time : 2022/6/15 11:17
DESC: 
"""
import csv

import pytest

from pythonProject_pytest.func.operation import my_add


def get_csv():
    """
    读取数据文件
    :return: 嵌套列表[(1,1,2)]
    """
    with open('../data/params.csv', 'r', encoding='utf-8') as file:
        raw = csv.reader(file)

        data = []
        for line in raw:
            data.append(line)
        print(data)
    return data


class TestWithCSV:
    @pytest.mark.parametrize('x,y,expected', get_csv())
    def test_addcsv(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)

