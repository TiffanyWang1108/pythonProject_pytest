"""
Name : conftest.py
Author  : Tiffany
Time : 2022/6/17 14:27
DESC: 
"""
import pytest
import yaml


def pytest_addoption(parser):
    # group 将下面所有的option都展示在这个group下
    mygrouop = parser.getgroup("hogwarts")

    mygrouop.addoption("--env",  # 注册一个命令行选项
                       default='test',  # 参数的默认值
                       dest='env',  # 存储的变量，为属性命令，可以使用option对象访问到这个值
                       help='set your run env'  # 帮助提示，参数的描述信息
                       )


@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env")
