#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/28 11:40
# @Author  : zheng
# @File    : test_payout.py
# @Software: PyCharm




import allure
import os
from case_data.api_data.payout_data import *
from testcase.payout.create import Create
import pytest
# from create_order_file import CreateOrder

@allure.epic("针对trade单元测试")
@allure.feature("付款接口")
class TestCreate:


    @allure.story('费率场景')
    @pytest.mark.parametrize("data, privateKey,merchant_fee,channel_fee, title", rate_case_payout)
    def test_xendit(self, data, privateKey, merchant_fee, channel_fee, title):
        allure.dynamic.title(f"{title}")
        Create().perform_payout(data, privateKey, merchant_fee=merchant_fee, channel_fee=channel_fee)

    @allure.story('路由用户标识')
    @pytest.mark.parametrize("data, privateKey, paychannel_code, title", user_routing_payout)
    def test_xendit(self, data, privateKey, paychannel_code, title):
        allure.dynamic.title(f"{title}")
        Create().perform_payout(data, privateKey, pay_channel=paychannel_code)

    @allure.story('普通路由场景')
    @pytest.mark.parametrize("data, privateKey, paychannel_code, title", normal_routing)
    def ordinary_route(self, data, privateKey, paychannel_code, title):
        allure.dynamic.title(f"{title}")
        Create().perform_payout(data, privateKey, pay_channel=paychannel_code)

    @allure.story("付款接口异常case合计")
    @pytest.mark.parametrize("data, privateKey, expected_code, expected_msg, title", payout_error_case)
    @pytest.mark.xfail     #断言失败则跳过
    def test_createorder_error(self,data, privateKey, expected_code, expected_msg, title):
            allure.dynamic.title(f"{title}")
            response = Create().perform_payout(data, privateKey, expected_code=expected_code, expected_msg=expected_msg)
            print(response)


    @allure.story("限额场景")
    @pytest.mark.parametrize("data, privateKey, expected_code, expected_msg, title", amount_limit_payout)
    @pytest.mark.xfail     #断言失败则跳过
    def test_createorder_error(self,data, privateKey, expected_code, expected_msg, title):
            allure.dynamic.title(f"{title}")
            response = Create().perform_payout(data, privateKey, expected_code=expected_code, expected_msg=expected_msg)
            print(response)


if __name__ == '__main__':
    if os.path.exists("D:/Tiki/results"):
        os.system("rm -r D:/Tiki/results")

    pytest.main(["-vs", '--alluredir', 'D:/Tiki/results'])

    # 生成allure报告
    os.system("allure generate D:/Tiki/results -o D:/Tiki/reports --clean")