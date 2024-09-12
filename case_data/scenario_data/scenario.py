#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/13 10:06
# @Author  : zheng
# @File    : scenario.py
# @Software: PyCharm
import yaml
order_true_qurest_data= [
# 商户id, 产品id, 币种，金额，支付方式，版本信息，， except_code, except_msg

        ( {
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR'
          },
        {
        'merchantId': '100119',
        'productId': '2023',
        'currency': 'IDR',
        'amount': '10000',
        'payChannel': '17',
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'
          },
         {'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'version' : '1.0',
         'orderType' : '0'
          },
          {
    'merchantId': '100119',
    'productId': '2023',
    'currency': 'IDR'
          },'97fa79f073c7c5e3c97b00b50b156eaa')
]

print(order_true_qurest_data)
order_fail_qurest_data= [
# 商户id, 产品id, 币种，金额，支付方式，版本信息，， except_code, except_msg

        ( {
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR'
          },
        {
        'merchantId': '100119',
        'productId': '2023',
        'currency': 'IDR',
        'amount': '10110',
        'payChannel': '17',
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'
          },
         {'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'version' : '1.0',
         'orderType' : '0'
          },
          {
    'merchantId': '100119',
    'productId': '2023',
    'currency': 'IDR'
          },'97fa79f073c7c5e3c97b00b50b156eaa')
]


