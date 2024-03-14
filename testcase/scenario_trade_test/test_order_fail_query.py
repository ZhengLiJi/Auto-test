#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/12 19:25
# @Author  : zheng
# @File    : test_order_true_query.py
# @Software: PyCharm
import pytest
import allure
from api.trade import Trade
from case_data.scenario_data.scenario import *
from lib.settings.get_time import GetTime
from lib.settings.logger import log

@allure.epic("针对收款业务场景的测试")
@allure.feature("下单成功，支付失败")
class TestOrderFailQurest:
    def setup_class(self):
        self.trade = Trade()
        self.time = GetTime()
        self.log = log

    @allure.story("用例--下单成功/支付失败/查询状态为99--预期成功")
    @allure.title("创建失败订单")
    @pytest.mark.parametrize('order_true_qurest_data', order_fail_qurest_data)
    def test_create_and_query_order(self, order_true_qurest_data):

        query_balance, create_order_data, query_order_data, query_balance2, privateKey = order_true_qurest_data
        self.log.info(f"{self.time.date_time_s()} *************** 开始执行用例 ***************")
        with allure.step("步骤1: 查询当前余额"):
            balance_before_order = self.trade.queryaccountbalance(query_balance, privateKey)
            allure.attach(f"下单前余额: {balance_before_order}", name="下单前余额")

        with allure.step("步骤2: 创建支付成功的订单"):
            create_order_data['orderNo'] = 'TestOrderNo_' + self.time.get_timestamp()
            order_resp = self.trade.create(create_order_data, privateKey)
            allure.attach(f"订单响应: {order_resp}", name="下单成功")

        with allure.step("步骤3: 查询订单是否为状态"):
            query_order_data["tradeNo"] = order_resp["tradeNo"]
            query_resp = self.trade.query(query_order_data, privateKey)
            allure.attach(f"查询响应: {query_resp}", name="查询订单状态是否为99")
            assert query_resp["payState"] == "11"

        with allure.step("步骤4: 订单支付失败，余额不变"):
            balance_after_order = self.trade.queryaccountbalance(query_balance2, privateKey)
            allure.attach(f"下单后余额: {balance_after_order}", name="下单后余额")
            assert balance_after_order['accountInfoList'][0]['balance'] == balance_before_order['accountInfoList'][0]['balance'] or \
                   balance_after_order['accountInfoList'][1]['balance'] == balance_before_order['accountInfoList'][1][ 'balance']
        self.log.info(f"{self.time.date_time_s()} *************** 用例执行结束 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_order_fail_qurest.py"])
    # os.system("allure generate D:/Tiki/results -o D:/Tiki/reports --clean")