#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/13 10:47
# @Author  : zheng
# @File    : 11.py
# @Software: PyCharm

PayCash = '82'
OXXO = '83'
MX_BANK_TRANSFER = '84'
from case_data.api_data.pay_channel import *
mx_normal_routing = [
    ({
         'merchantId': mx_merchantId,
         'productId': mx_productId,
         'currency': currency_MXN,
         'amount': '10',
         'payChannel': MX_BANK_TRANSFER,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, mx_key, '200', "the order amount is too small",
     "支付"),

    ({
         'merchantId': mx_merchantId,
         'productId': mx_productId,
         'currency': currency_MXN,
         'amount': '100',
         'payChannel': OXXO,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, mx_key, '200', "the order amount is too big",
     "指定商户钱包类型最大限额为100000"),

    ({
         'merchantId': mx_merchantId,
         'productId': mx_productId,
         'currency': currency_MXN,
         'amount': '100',
         'payChannel': PayCash,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, mx_key, '88026', "the order amount is too small",
     "指定商户的支付方式DANA类型最小限额为100000"),


] #商户下单