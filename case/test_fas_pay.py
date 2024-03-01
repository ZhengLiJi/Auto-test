import allure
import pytest
import time
import os
from lib.create_order2 import CreateOrder
from case_data.idr_data import xendit1_data

# 你的Test_create_order就是父类 case层不应该加上api的请求逻辑和参数拼接， 需要的是直接把参数给接口，然后拿返回，再判断你这次组装的 {符合你业务的数据} 【返回的结果】是否符合你的 [预期值]
# 比如你的ovo_success 你的业务数据 = '100119', '2023', "IDR", '20110', '081382826304', '15', '97fa79f073c7c5e3c97b00b50b156eaa' 返回的结果就是result assert就是把实际结果和你的预期进行判断
import pytest

import pytest
# from create_order_file import CreateOrder


class TestCreateOrder:
    @allure.title('xendit1qudao')
    @pytest.mark.parametrize("data", xendit1_data)
    def test_create_order(self, data):
        # 创建 CreateOrder 实例
        create_order_xendit = CreateOrder()

        # 从 data 字典中提取参数
        merchantId = data['merchantId']
        productId = data['productId']
        currency = data['currency']
        amount = data['amount']
        payerPhone = data['payerPhone']
        payChannel = data['payChannel']
        privateKey = data['privateKey']

        # 调用 create_order 方法发送请求并获取结果
        result = create_order_xendit.create_order(merchantId, productId, currency, amount, payerPhone,
                                                    payChannel, privateKey)

        # 执行断言，比如检查返回结果是否符合预期
        assert result.get('code') == '200', f"断言失败: 实际结果为 {result.get('code')}, 期望结果为 '200'"



if __name__ == '__main__':

    pytest.main(["-vs", '--alluredir', 'D:/Tiki/results'])

    # 生成allure报告
    os.system("allure generate D:/Tiki/results -o D:/Tiki/reports --clean")