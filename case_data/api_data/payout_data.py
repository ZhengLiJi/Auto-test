#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/28 9:47
# @Author  : zheng
# @File    : payout_data.py
# @Software: PyCharm
from case_data.api_data.pay_channel import *


user_routing_payout = [
     ({
          'merchantId': merchantId_119,
          'productId': productId_119,
          'currency': currency_IDR,
          'amount': '10000',
          'accountNumber': '0888888881',
          'bankCode': 'DANA',
          'version': 1.0,
          'description': 'test',
          'accountHolderName': 'user_xendit'
     },
     key_119, xendit, "xendit"),


     ({
           'merchantId': merchantId_119,
           'productId': productId_119,
           'currency': currency_IDR,
           'amount': '10000',
           'accountNumber': '0888888881',
           'bankCode': 'DANA',
           'version': 1.0,
           'description': 'test',
           'accountHolderName': 'user_mpi'
      },
      key_119, mpi, "mpi"),

     ({
           'merchantId': merchantId_119,
           'productId': productId_119,
           'currency': currency_IDR,
           'amount': '10000',
           'accountNumber': '0888888881',
           'bankCode': 'DANA',
           'version': 1.0,
           'description': 'test',
           'accountHolderName': 'user_gv'
      },
      key_119, gv, "gv"),

     ({
           'merchantId': merchantId_119,
           'productId': productId_119,
           'currency': currency_IDR,
           'amount': '10000',
           'accountNumber': '0888888881',
           'bankCode': 'DANA',
           'version': 1.0,
           'description': 'test',
           'accountHolderName': 'user_faspay'
      },
      key_119, faspay, "faspay"),

     ({
           'merchantId': merchantId_119,
           'productId': productId_119,
           'currency': currency_IDR,
           'amount': '10000',
           'accountNumber': '0888888881',
           'bankCode': 'DANA',
           'version': 1.0,
           'description': 'test',
           'accountHolderName': 'user_dana'
      },
      key_119, dana_channel, "dana"),

     ({
           'merchantId': merchantId_119,
           'productId': productId_119,
           'currency': currency_IDR,
           'amount': '10000',
           'accountNumber': '0888888881',
           'bankCode': 'DANA',
           'version': 1.0,
           'description': 'test',
           'accountHolderName': 'user_oy'
      },
      key_119, oy, "oy"),


]

payout_error_case = [
    ({
         'merchantId': 119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '', "merchantid不存在"),

    ({
         'merchantId': "",
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '', "merchantid不为空"),

    ({
         'merchantId': "sad1231",
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '', "merchantid只接受纯数字"),

    ({
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '',  "merchantid为必传参数"),

    ({
         'merchantId': merchantId_119,
         'productId': 1212,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '', "productId不存在"),

    ({
         'merchantId': merchantId_119,
         'productId': '',
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '', "productId不为空"),

    ({
         'merchantId': merchantId_119,
         'productId': 'sada12',
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '', "productId只接受纯数字"),

    ({
         'merchantId': merchantId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '', "productId为比传参数"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDS',
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '', "currency不存在"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': '',
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '', "currency不为空"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '', "currency为必传参数"),
]