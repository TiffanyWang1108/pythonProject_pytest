"""
Name : test_addjson.py
Author  : Tiffany
Time : 2022/6/15 11:44
DESC: 
"""
import json

import pytest

from pythonProject_pytest.func.operation import my_add


def get_json():
    with open('../data/params.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        # print(data)
        # print(list(data.values()))
    return list(data.values())


class TestWithJSON:
    @pytest.mark.parametrize('x,y,expected', get_json())
    def test_add(self, x, y, expected):
        value = my_add(int(x), int(y))
        assert value == int(expected)

