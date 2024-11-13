#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/25 14:55
# @Author  : zheng
# @File    : sql.py
# @Software: PyCharm
from lib.utils.database.mysql.sql_warp import *
class Sql:

    @staticmethod
    def order_bill_select(tradeno):
        a = Dbtrade().search(f"select * from order_bill where trade_no = {tradeno}")
        print(a)
        return a

    @staticmethod
    def settlment_select(field,tradeno):
        a = Dbtrade()
        b = a.search(f"select * from settlement_record where trade_no = {tradeno}")
        print(b)
        return b

    @staticmethod
    def account_keep_log(oo,tradeno):
        a = Dbusercenter().search(f"select * from {oo} where trade_no = {tradeno}")
        assert a is not None and a != [], "查询结果为空或为 None"


if __name__ == '__main__':
    c = Sql().order_bill_select('10012024042514123272900008')
    print(c)



