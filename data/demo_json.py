"""
Name : demo_json.py
Author  : Tiffany
Time : 2022/6/15 11:35
DESC: 
"""
import json


def get_json():
    with open('demo.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())  # loads--将json文本解析成字符串
        print(type(data), data)

        s = json.dumps(data, ensure_ascii=False)  # dumps--将字符串封装成json数据
        print(s, type(s))


if __name__ == '__main__':
    get_json()