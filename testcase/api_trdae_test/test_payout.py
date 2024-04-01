#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/28 11:40
# @Author  : zheng
# @File    : test_payout.py
# @Software: PyCharm




import allure
import os
from api.trade import Trade
from common.mysql import MysqlDb
from lib.create_payout import Payout
from lib.settings.logger import log
from lib.settings.get_time import GetTime
from case_data.api_data.idr_data import *
from case_data.api_data.payout_data import *
import ast
import pytest

# from create_order_file import CreateOrder

@allure.epic("针对trade单元测试")
@allure.feature("付款接口")
class TestCreate:
    def setup_class(self):
        self.xxx = Trade()
        # self.log = log
        # self.time = GetTime()
        # self.xxx.log.info()
        self.mysql = MysqlDb('trade')
        self.account_mysql = MysqlDb('usercenter')
    # 这个接口 对你来说 是一个功能接口， 你要实现的是完成这个接口场景 需要搭配不同的参数 但是实际上你这个接口在runtestcase是不希望他单独运行吧
    def perform_order_test(self, data, privateKey, expected_code=None, expected_msg=None, expected_type=None, orderNo=None,
                           merchant_fee=None,channel_fee=None, pay_channel=None):
        if orderNo is not None and 'orderNo' not in data:
            # 如果 orderNo 存在且 data 中没有 orderNo 字段，则将 orderNo 添加到 data 中
            data['orderNo'] = orderNo
        elif 'orderNo' not in data:
            data['orderNo'] = 'TestOrderNo_' + self.time.get_timestamp()

        self.log.info(f"{self.time.date_time_s()} *************** 开始执行用例 ***************")
        queryaccountbalance = self.account_mysql.select_db(f"select * from account_info where user_id = '{data['merchantId']}'")
        assert queryaccountbalance, f"数据库中未找到订单号为 {data['merchantId']} 的记录"
        result = self.xxx.payout(data, privateKey)

        if pay_channel is not None or merchant_fee is not None:
            # 如果传入了 pay_channel 或 fee_rate，则要断言是否返回 200
            try:
                assert result.get('code') == '200', "预期状态码为 200，实际状态码为 {}".format(result.get('code'))
            except AssertionError as e:
                raise AssertionError(f"{e}")

            # 查询订单数据
            order_data = self.mysql.select_db(f"select * from payout_bill where order_no = '{result.get('orderNo')}'")
            assert order_data, f"数据库中未找到订单号为 {data('orderNo')} 的记录"
            #查询商户余额是否扣减

            if pay_channel is not None:
                assert order_data[0]['pay_channel'] == pay_channel, f"支付渠道不符合预期，实际值为 {order_data[0]['pay_channel']}"
                # 如果传入了 pay_channel，则断言支付渠道,路由场景。

                queryaccountbalance2 = self.mysql.select_db(
                f"select * from account_info where user_id = '{data['merchantId']}'")
                assert queryaccountbalance[0]['balance'] < queryaccountbalance2[0]['balance'], "第一次查询结果的余额小于第二次查询结果的余额"

            if merchant_fee is not None:
                    # 如果传入了 merchant_fee，则断言费率，费率场景，查看商户费率是否正常扣除
                    try:
                        assert order_data[0]['merchant_fee'] == merchant_fee, f"费率不符合预期，实际值为 {order_data[0]['merchant_fee']}" #普通的商户费率

                    except AssertionError as e:
                        raise AssertionError(f"{e}")

                    if channel_fee is not None:
                        assert order_data[0][
                                   'channel_fee'] == channel_fee, f"费率不符合预期，实际值为 {order_data[0]['channel_fee']}"  #渠道费率


            else:
                # 如果 pay_channel 和 merchant_fee 都没有传入，则默认执行状态码和消息类型的断言
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

            self.log.info(f"{self.time.date_time_s()} *************** 执行用例结束 ***************")

    # @allure.story('费率场景')
    # @pytest.mark.parametrize("data, privateKey,merchant_fee,channel_fee, title", rate_case)
    # def test_xendit(self, data, privateKey, merchant_fee, channel_fee, title):
    #     allure.dynamic.title(f"{title}")
    #     self.perform_order_test(data, privateKey, merchant_fee=merchant_fee, channel_fee=channel_fee)
    #

    @allure.story('路由用户标识')
    @pytest.mark.parametrize("data, privateKey, paychannel_code, title", user_routing_payout)
    def test_xendit(self, data, privateKey, paychannel_code, title):
        allure.dynamic.title(f"{title}")
        self.perform_order_test(data, privateKey, pay_channel=paychannel_code)

    # @allure.story('路由金额区间')
    # @pytest.mark.parametrize("data, privateKey,paychannel_code, title", amount_routing)
    # def test_xendit(self, data, privateKey, paychannel_code, title):
    #     allure.dynamic.title(f"{title}")
    #     self.perform_order_test(data, privateKey, pay_channel=paychannel_code)

    # @allure.story('普通路由场景')
    # @pytest.mark.parametrize("data, privateKey, paychannel_code, title", xendit1_data)
    # def ordinary_route(self, data, privateKey, paychannel_code, title):
    #     allure.dynamic.title(f"{title}")
    #     self.perform_order_test(data, privateKey, pay_channel=paychannel_code)


    # @allure.story("下单接口异常case合计")
    # @pytest.mark.parametrize("data, privateKey, expected_code, expected_msg, title", create_order_data)
    # @pytest.mark.xfail     #断言失败则跳过
    # def test_createorder_error(self,data, privateKey, expected_code, expected_msg, title):
    #         allure.dynamic.title(f"{title}")
    #         response = self.perform_order_test(data, privateKey, expected_code=expected_code, expected_msg=expected_msg)
    #         print(response)

    # @allure.story("限额场景")
    # @pytest.mark.parametrize("data, privateKey, expected_code, expected_msg, title", amount_lmiti)
    # @pytest.mark.xfail     #断言失败则跳过
    # def test_createorder_error(self,data, privateKey, expected_code, expected_msg, title):
    #         allure.dynamic.title(f"{title}")
    #         response = self.perform_order_test(data, privateKey, expected_code=expected_code, expected_msg=expected_msg)
    #         print(response)

    @allure.epic()
    @pytest.mark.parametrize("base_url, data, ")
    def test_payout_payout(self,):
        Payout().send_post_request()


if __name__ == '__main__':
    if os.path.exists("D:/Tiki/results"):
        os.system("rm -r D:/Tiki/results")

    pytest.main(["-vs", '--alluredir', 'D:/Tiki/results'])

    # 生成allure报告
    os.system("allure generate D:/Tiki/results -o D:/Tiki/reports --clean")