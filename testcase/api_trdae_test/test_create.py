import allure
import os
from api.trade import Trade
from lib.settings.logger import log
from lib.settings.get_time import GetTime
from case_data.api_data.idr_data import *
from case_data.api_data.order_data import *

import pytest
# from create_order_file import CreateOrder

@allure.feature("监控各下单")
class TestCreate:
    def setup_class(self):
        self.xxx = Trade()
        self.log = log
        self.time = GetTime()

    def perform_order_test(self, data, privateKey, expected_code, expected_msg=None, expected_type=None, orderNo=None):
        if orderNo is not None and 'orderNo' not in data:
            # 如果 orderNo 存在且 data 中没有 orderNo 字段，则将 orderNo 添加到 data 中
            data['orderNo'] = orderNo
        elif 'orderNo' not in data:
            data['orderNo'] = 'TestOrderNo_' + self.time.get_timestamp()
        result = self.xxx.create(data,privateKey)
        try:
            assert result.get('code') == expected_code and (
                    (expected_msg and result.get('msg') == expected_msg) or
                    (expected_type and result.get('type') == expected_type)
            ), (
                f"断言失败: 实际结果为 {result.get('code')},{result.get('msg') or result.get('type')} "
                f"期望结果为 {expected_code}. {expected_msg or expected_type}"
            )
        except AssertionError as e:
            raise AssertionError(f"{e}")

    # @allure.story("xendit渠道")
    # @allure.title('xendit渠道下单')
    # @pytest.mark.parametrize("data, privateKey,expected_code,expected_msg", xendit1_data)
    # def test_xendit(self, data, privateKey, expected_code, expected_msg):
    #     self.perform_order_test(data, privateKey, expected_code, expected_msg)

    @allure.story("下单接口异常case合计")
    @pytest.mark.parametrize("data, privateKey, expected_code, expected_msg, title", create_order_data)
    @pytest.mark.xfail     #断言失败则跳过
    def test_createorder_error(self,data, privateKey, expected_code, expected_msg, title):
            allure.dynamic.title(f"{title}")
            response = self.perform_order_test(data, privateKey, expected_code, expected_msg)
            print(response)



if __name__ == '__main__':
    if os.path.exists("D:/Tiki/results"):
        os.system("rm -r D:/Tiki/results")

    pytest.main(["-vs", '--alluredir', 'D:/Tiki/results'])

    # 生成allure报告
    os.system("allure generate D:/Tiki/results -o D:/Tiki/reports --clean")