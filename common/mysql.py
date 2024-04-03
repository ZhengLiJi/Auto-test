#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/15 17:33
# @Author  : zheng
# @File    : mysql.py
# @Software: PyCharm
import pymysql
from lib.base_utils import log


class MysqlDb:

    def __init__(self, db):
        self.db = db
        self.conn = None
        self.cur = None

    def __enter__(self):
        self.conn = pymysql.connect(host='149.129.247.24', user='root', password='#Love1992', db=self.db, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def select_db(self, sql):
        """查询"""
        try:
            self.__enter__()  # 打开数据库连接
            self.conn.ping(reconnect=True)
            self.cur.execute(sql)
            return self.cur.fetchall()
        except Exception as e:
            log.error("操作MySQL出现错误，错误原因：{}".format(e))
            raise  # 抛出异常，让调用者处理

    def execute_db(self, sql):
        """更新/新增/删除"""
        try:
            self.__enter__()  # 打开数据库连接
            self.conn.ping(reconnect=True)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            log.error("操作MySQL出现错误，错误原因：{}".format(e))
            self.conn.rollback()
            raise
        finally:
            self.__exit__(None, None, None)  # 关闭数据库连接


if __name__ == '__main__':
    order = MysqlDb("trade").select_db('select * from order_bill where trade_no = "10012024031511045516800007"')
    print(order)