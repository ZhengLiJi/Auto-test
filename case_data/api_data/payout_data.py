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


] #用户标识路由

normal_routing = [
    ({
        'merchantId': merchantId_149,
        'productId': productId_149,
        'currency': 'IDR',
        'amount': '100000',
        'payChannel': bri,
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'},
    key_149, xendit, "单个类型的普通路由"),

    ({
        'merchantId': merchantId_149,
        'productId': productId_149,
        'currency': 'IDR',
        'amount': '100000',
        'payChannel': linkaja,
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'},
    key_149, xendit, "单个支付方式的普通路由"),

    ({
         'merchantId': merchantId_149,
         'productId': productId_149,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': cimb,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_149, oy, "多个支付方式的普通路由"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '100000',
         'payChannel': bri,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, oy, "单个商户及单个类型的普通路由"),

    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '100000',
         'payChannel': shopeepay,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_888, xendit, "多个商户及单个类型的普通路由"),

    ({
        'merchantId': merchantId_119,
        'productId': productId_119,
        'currency': 'IDR',
        'amount': '100000',
        'payChannel': dana,
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'},
    key_119, mpi, "单个商户及单个支付方式的普通路由"),

    ({
         'merchantId': merchantId_149,
         'productId': productId_149,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_149, dana_channel, "单个商户及多个支付方式的普通路由"),

    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '100000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_888, oy, "多个商户及单个支付方式的普通路由"),

    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '100000',
         'payChannel': linkaja,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_888, oy, "多个商户及多个支付方式的普通路由"),

] #普通路由

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
     key_119, '88070', 'merchant permission is not supported', "merchantid不存在"),

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
     key_119, '88070', 'merchant permission is not supported', "merchantid不为空"),

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
     key_119, '88070', 'merchant permission is not supported', "merchantid只接受纯数字"),

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
     key_119, '88070', 'merchant permission is not supported',  "merchantid为必传参数"),

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
     key_119, '88032', 'productId is not valid', "productId不存在"),

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
     key_119, '88001', ' ', "productId不为空"),

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
     key_119, '88001', 'length of currency field is too long', "currency不为空"),

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
     key_119, '88001', 'currency can not be blank', "currency为必传参数"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000.11',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88048', 'amount should be integer', "amount金额不接受小数点"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000zxa',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', '', "amout金额只接受数字"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', 'amount can not be blank', "amout金额不为空"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', 'amount can not be blank', "amout是必传参数"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANAz',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88011', 'this channel is not supported yet', "bankCode不存在"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': '',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', 'length of bankCode field is too long', "bankCode为空"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', 'bankCode can not be blank ', "bankCode是必传参数"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': '',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', 'length of description field is too long', "description不为空"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', 'description can not be blank', "description为必填参数"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88040', 'phone of ewallet payout must start with 08', "支付方式为钱包的必须为08开头"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '',
         'bankCode': 'BNI',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', 'length of accountNumber field is too long', "accountNumber不为空"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'bankCode': 'BNI',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, '88001', 'accountNumber can not be blank', "accountNumber为必传参数"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': ''
     },
     key_119, '88001', 'length of accountHolderName field is too long', "accountHolderName不为空"),


] #异常case

amount_limit_payout = [
    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '9',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'tets'
     },
     key_119, '88026', "the order amount is too small",
     "指定商户钱包类型最小限额为10000"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '5000001',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'test'
     },
     key_119, '88036', "the order amount is too big",
     "指定商户钱包类型最小限额为10000"),

] #商户限额场景

idempotence_payout = [
    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '5000001',
         'accountNumber': '0888888881',
         'bankCode': 'DANA',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'test'
     },
     key_119, '88003', "the order amount is too small",
     "幂等性")
] #幂等性问题

rate_case_payout = [
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
     key_119, 5000, 6000, "商户和渠道的基础费率"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': currency_IDR,
         'amount': '10000',
         'accountNumber': '0888888881',
         'bankCode': 'BNI',
         'version': 1.0,
         'description': 'test',
         'accountHolderName': 'user_xendit'
     },
     key_119, 201, 3100, "商户和渠道的基础费率+比例费率"),
] #费率场景


