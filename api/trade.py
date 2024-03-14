#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/7 21:16
# @Author  : zheng
# @File    : trade.py
# @Software: PyCharm
import allure

from lib.create_payout import Payout

class Trade(Payout):

    def payout(self,data,private_key):
        self.setup(data, private_key)
        resp = self.post_sit(url="/pay/payout", desc='付款接口')
        return resp
        # assert result(resp), "Assertion failed for payout request"

    def refund(self, data, private_key,):
        self.setup(data, private_key)
        resp = self.post_sit(url="/pay/refund", desc='退款接口')
        return resp

    def queryaccountbalance(self, data, privateKey):
        # data['orderNo'] = 'TestOrderNo_' + self.time.get_timestamp()
        self.setup(data, privateKey)
        resp = self.post_sit(url="/accountInfo/queryAccountBalance", desc='余额查寻接口')
        return resp

    def create(self, data, privateKey):

        self.setup(data, privateKey)
        resp = self.post_sit(url="/pay/createOrder", desc='支付接口')
        return resp
    #
    def query(self,data,private_key):
        self.setup(data,private_key)
        resp = self.post_sit(url="/pay/queryOrder", desc= "订单查询接口")
        return resp

    def award(self, data, privateKey):
        self.setup(data, privateKey)
        resp = self.post_sit(url="/pay/award", desc='奖励发放接口')
        return resp

    def query_award_list(self, data, privateKey):
        self.setup(data, privateKey)
        resp = self.post_sit(url="/pay/queryAwardList", desc='查询奖励发放产品列表')
        return resp

    def recurring(self, data, privateKey):
        self.setup(data, privateKey)
        resp = self.post_sit(url="/recurring/createRecurring", desc='订阅接口')
        return resp

    def query_recurring(self, data, privateKey):
        self.setup(data, privateKey)
        resp = self.post_sit(url="/recurring/queryRecurring", desc='查询订阅接口')
        return resp

    def stop_recurring(self, data, privateKey):
        self.setup(data, privateKey)
        resp = self.post_sit(url="/recurring/stopRecurring", desc='取消订阅接口')
        return resp




            # 返回响应

    # def quest(self):
if __name__ == '__main__':
    pass