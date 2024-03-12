import allure
import pytest
import time
import os
from lib.create_order2 import CreateOrder
from case_data.idr_data import *

# 你的Test_create_order就是父类 case层不应该加上api的请求逻辑和参数拼接， 需要的是直接把参数给接口，然后拿返回，再判断你这次组装的 {符合你业务的数据} 【返回的结果】是否符合你的 [预期值]
# 比如你的ovo_success 你的业务数据 = '100119', '2023', "IDR", '20110', '081382826304', '15', '97fa79f073c7c5e3c97b00b50b156eaa' 返回的结果就是result assert就是把实际结果和你的预期进行判断
import pytest

import pytest


# from create_order_file import CreateOrder

@allure.feature("监控各下单")
class TestCreateOrder:
    def setup_class(self):
        self.order = CreateOrder()

    # 你丢了一个object进来？ 啊？
    def perform_order_test(self, data, expected_code):
        merchantId = data['merchantId']
        productId = data['productId']
        currency = data['currency']
        amount = data['amount']
        payerPhone = data['payerPhone']
        payChannel = data['payChannel']
        privateKey = data['privateKey']
        result = self.order.create_order(merchantId, productId, currency, amount, payerPhone, payChannel,
                                   privateKey)
        assert result.get(
            'code') == expected_code, f"断言失败: 实际结果为 {result.get('code')}, 期望结果为 {expected_code}"

    @allure.story("xendit渠道")
    @allure.title('xendit渠道下单')
    @pytest.mark.parametrize("data, expected_code", xendit1_data)
    # @pytest.fixture
    def test_xendit(self, data, expected_code):
        self.perform_order_test(data, expected_code)

        # 可以了ok。
    # @allure.story("OY渠道")
    # @allure.title('OY渠道下单')
    # @pytest.mark.parametrize("data, expected_code", oy_data)
    # # @pytest.fixture
    # def test_oy(self, create_order_oy, data, expected_code):
    #     TestCreateOrder().perform_order_test(create_order_oy, data, expected_code)


if __name__ == '__main__':
    # if os.path.exists("D:/Tiki/results"):
    #     os.system("rm -r D:/Tiki/results")

    pytest.main(['D:/Tiki/case/test_create_order.py', "-vs", '--alluredir', 'D:/Tiki/results'])

    # 生成allure报告
    os.system("allure generate D:/Tiki/results -o D:/Tiki/results/reports --clean")
