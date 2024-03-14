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
import os
@allure.epic("针对收款业务场景的测试")
@allure.feature("下单成功，支付成功，回调成功，记账成功，插入结算账单")
class TestOrderTrueQurest:
        def setup_class(self):
            self.trade = Trade()
            self.time = GetTime()

        @allure.story("用例--查询余额/下单成功/回调成功/查询余额，余额增加/结算--预期成功")
        @allure.title("创建支付成功订单")
        @pytest.mark.parametrize('order_true_qurest_data', order_true_qurest_data)
        def test_create_and_query_success_order(self, order_true_qurest_data):


            query_balance, create_order_data, query_order_data, query_balance2, privateKey = order_true_qurest_data

            with allure.step("步骤1: 查询订单前余额"):
                balance_before_order = self.trade.queryaccountbalance(query_balance, privateKey)
                allure.attach(f"下单前余额: {balance_before_order}", name="下单前余额")

            with allure.step("步骤2: 创建成功订单"):
                create_order_data['orderNo'] = 'TestOrderNo_' + self.time.get_timestamp()
                order_resp = self.trade.create(create_order_data, privateKey)
                allure.attach(f"订单响应: {order_resp}", name="创建订单响应")

            with allure.step("步骤3: 查询订单状态是否为成功"):
                query_order_data["tradeNo"] = order_resp["tradeNo"]
                query_resp = self.trade.query(query_order_data, privateKey)
                allure.attach(f"查询响应: {query_resp}", name="查询订单状态响应码是否为200")
                assert query_resp["payState"] == "00"

            with allure.step("步骤4: 余额或待结算余额增加"):
                balance_after_order = self.trade.queryaccountbalance(query_balance2, privateKey)
                allure.attach(f"下单后余额: {balance_after_order}", name="下单后余额")
                assert balance_after_order['accountInfoList'][0]['balance'] == \
                       balance_before_order['accountInfoList'][0]['balance'] or \
                       balance_after_order['accountInfoList'][1]['balance'] == \
                       balance_before_order['accountInfoList'][1]['balance']



if __name__ == '__main__':
    pytest.main(["-vs", '--alluredir', 'D:/Tiki/results'])

    # 生成allure报告
    os.system("allure generate D:/Tiki/results -o D:/Tiki/reports --clean")
