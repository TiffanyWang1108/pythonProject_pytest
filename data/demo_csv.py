"""
Name : demo_csv.py
Author  : Tiffany
Time : 2022/6/15 11:07
DESC: 
"""
import csv


def get_csv():
    with open("demo.csv", 'r', encoding='utf-8') as file:
        raw = csv.reader(file)  # 返回的是一个迭代对象

        for line in raw:
            print(line)


if __name__ == '__main__':
    get_csv()
