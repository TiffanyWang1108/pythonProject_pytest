"""
Name : test_add.py
Author  : Tiffany
Time : 2022/6/14 18:50
DESC: 
"""
import openpyxl
import pytest

from pythonProject_pytest.func.operation import my_add


def get_excel():
    """

    :return:[(1,1,2), (3,6,9),(100,200,300)]
    """
    # 获取工作表文件
    book = openpyxl.load_workbook("../data/params.xlsx")
    # 获取工作表sheet
    sheet = book.active
    # 读取数据
    cell = sheet['A1':'C3']
    print(cell)  # 是一个嵌套元组
    values = []
    for row in cell:
        data = []
        for cell in row:
            data.append(cell.value)
        values.append(data)

    print(values)
    return values


class TestWithExcel:
    @pytest.mark.parametrize('x,y,expected', get_excel())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
