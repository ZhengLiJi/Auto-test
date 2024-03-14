#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 15:29
# @Author  : zheng
# @File    : dataloader.py
# @Software: PyCharm

# 您的代码几乎完成了，但有一个小错误和一个潜在的改进点：
#
# 错误：在 load_yaml_file 方法的末尾，您调用了 load_yaml_file 方法，但没有使用它返回的数据。相反，您应该使用 load_and_unpack_yaml 方法，因为它调用 unpack_test_data 方法来处理数据。
#
# 潜在的改进点：在 load_yaml_file 方法中，建议使用 yaml.safe_load() 而不是 yaml.load() 来加载 YAML 文件，以提高安全性。
#
# 这里是修正后的代码：
#
# python
# Copy code
import yaml

class DataLoader:
    @staticmethod
    def load_yaml_file(file_path):
        """Load data from a YAML file"""
        with open(file_path, 'r', encoding='utf-8') as file:  # 修改编码方式
            yaml_data = yaml.safe_load(file)
            print("Loaded YAML data:", yaml_data)  # 添加调试语句
            return yaml_data

    @staticmethod
    def unpack_test_data(test_data):
        unpacked_data = []
        for data in test_data:
            if isinstance(data, dict):
                unpacked_data.append(tuple(data.values()))
            else:
                unpacked_data.append(data)
        return unpacked_data

    @classmethod
    def load_and_unpack_yaml(cls, file_path):
        """Load YAML file and unpack test data"""
        test_data = cls.load_yaml_file(file_path)
        return cls.unpack_test_data(test_data)

if __name__ == '__main__':
    test_data = DataLoader.load_yaml_file(r'D:\Tiki\case_data\api_data\create_order_data.yaml')
