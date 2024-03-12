import allure
import pytest
import time
import os
from api.trade import Trade
from case_data.order_data  import *


# 你的Test_create_order就是父类 case层不应该加上api的请求逻辑和参数拼接， 需要的是直接把参数给接口，然后拿返回，再判断你这次组装的 {符合你业务的数据} 【返回的结果】是否符合你的 [预期值]
# 比如你的ovo_success 你的业务数据 = '100119', '2023', "IDR", '20110', '081382826304', '15', '97fa79f073c7c5e3c97b00b50b156eaa' 返回的结果就是result assert就是把实际结果和你的预期进行判断
import pytest

import pytest
# from create_order_file import CreateOrder

@allure.feature("监控各下单")
class TestCreate:
    def setup_class(self):
        self.xxx = Trade()

    def perform_order_test(self, data, privateKey, expected_code, expected_msg=None, expected_type=None):
        result = self.xxx.create(data,privateKey)
        try:
            assert result.get('code') == expected_code and (
                    (expected_msg and result.get('msg') == expected_msg) or
                    (expected_type and result.get('type') == expected_type)
            ), (
                f"断言失败: 实际结果为 {result.get('code')}, "
                f"期望结果为 {expected_code}. {expected_msg or expected_type}"
            )
        except AssertionError as e:
            print(f"断言失败: {e}")

    # @allure.story("xendit渠道")
    # @allure.title('xendit渠道下单')
    # @pytest.mark.parametrize("data, privateKey,expected_code", xendit1_data)
    # def test_xendit(self, data, privateKey, expected_code, expected_msg):
    #     self.perform_order_test(data, privateKey, expected_code, expected_msg)

    @allure.story("下单接口异常case合计")
    def test_createorder_error(self):
        for data, privateKey, expected_code, expected_msg, title in error_data:
            allure.dynamic.title(f"下单接口 - {title}")  # 设置标题
            self.perform_order_test(data, privateKey, expected_code, expected_msg)








    # @allure.story("OY渠道")
    # @allure.title('OY渠道下单')
    # @pytest.mark.parametrize("data, expected_code", oy_data)
    # # @pytest.fixture
    # def oy_test(self, create_order_oy, data, expected_code):
    #     TestCreate().perform_order_test(create_order_oy, data, expected_code)



if __name__ == '__main__':
    # if os.path.exists("D:/Tiki/results"):
    #     os.system("rm -r D:/Tiki/results")

    pytest.main(["-vs", '--alluredir', 'D:/Tiki/results'])

    # 生成allure报告
    os.system("allure generate D:/Tiki/results -o D:/Tiki/results/reports --clean")