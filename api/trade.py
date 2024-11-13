#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/7 21:16
# @Author  : zheng
# @File    : trade.py
# @Software: PyCharm

import allure
from lib.create_payout import Payout


class Trade(Payout):
    def __init__(self, env="sit"):
        self.env = env

    def request(self, data, private_key, endpoint, desc):
        self.setup(data, private_key)
        return self.post(self.env, url=endpoint, desc=desc)

    def payout(self, data, private_key):
        return self.request(data, private_key, "/pay/payout", '付款接口')

    def refund(self, data, private_key):
        return self.request(data, private_key, "/pay/refund", '退款接口')

    def query_account_balance(self, data, private_key):
        return self.request(data, private_key, "/accountInfo/queryAccountBalance", '余额查询接口')

    def create(self, data, private_key):
        return self.request(data, private_key, "/pay/createOrder", '支付接口')

    def query(self, data, private_key):
        return self.request(data, private_key, "/pay/queryOrder", '订单查询接口')

    def award(self, data, private_key):
        return self.request(data, private_key, "/pay/award", '奖励发放接口')

    def query_award_list(self, data, private_key):
        return self.request(data, private_key, "/pay/queryAwardList", '查询奖励发放产品列表')

    def recurring(self, data, private_key):
        return self.request(data, private_key, "/recurring/createRecurring", '订阅接口')

    def query_recurring(self, data, private_key):
        return self.request(data, private_key, "/recurring/queryRecurring", '查询订阅接口')

    def stop_recurring(self, data, private_key):
        return self.request(data, private_key, "/recurring/stopRecurring", '取消订阅接口')


    def encryptCoinPay_createOrder(self, data, private_key):
        return self.request(data, private_key, "/encryptCoinPay/createOrder", '虚拟币下单接口')

    def encryptCoinPay_payout(self, data, private_key):
        return self.request(data, private_key, "/encryptCoinPay/payout", '虚拟币付款接口')

    def encryptCoinPay_queryOrder(self, data, private_key):
        return self.request(data, private_key, "/encryptCoinPay/queryOrder", '查询接口')

if __name__ == '__main__':
    trade = Trade(env='sit')  # 可选择不同的环境，例如'sit', 'pg', 'la', 等
    response = trade.create(data={'example_key': 'example_value'}, private_key='your_private_key')
    print(response)




