"""
Name : demo_try.py
Author  : Tiffany
Time : 2022/6/14 16:03
DESC: 
"""
try:
    a = int(input('输入被除数： '))
    b = int(input('输入除数： '))
    c = a / b
    print('两数相除的结果是：', c)
except(ValueError, ArithmeticError):
    print("值异常、算数异常")
except:
    print("未知异常")
print("continue")
