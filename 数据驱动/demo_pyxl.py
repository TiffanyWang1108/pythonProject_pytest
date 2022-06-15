"""
Name : demo_pyxl.py
Author  : Tiffany
Time : 2022/6/14 18:17
DESC: 
"""
import openpyxl


# 获取excel文件
book = openpyxl.load_workbook("params.xlsx")


# 获取工作表
sheet = book.active
# 获取单元格数据
a_1 = sheet['A1'].value
print(a_1)
c_3 = sheet.cell(column=3, row=3).value
print(c_3)


# 获取多个单元格数据
cells = sheet['A1':'c3']
print(type(cells), cells)
