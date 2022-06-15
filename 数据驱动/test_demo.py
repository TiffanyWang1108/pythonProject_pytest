"""
Name : test_demo.py
Author  : Tiffany
Time : 2022/6/14 18:03
DESC: 
"""
import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):
        if "test" in env:
            print('这是测试环境')
            print(env)  # 只打印字典中的key,在yaml文件中加入- 回车和空格变为列表嵌套字典
            print("测试环境的ip是：", env["test"])
        elif "dev" in env:
            print("这是开发环境")

    def test_yaml(self):
        print(yaml.safe_load(open("./env.yml")))


