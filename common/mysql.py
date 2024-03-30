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
        # 通过字典拆包传递配置信息，建立数据库连接
        self.db = db
        self.conn = pymysql.connect(host='149.129.247.24', user='root', password='#Love1992', db=db, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def close(self):
        self.cur.close()
        self.conn.close()

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        self.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        self.close()
        return data

    def execute_db(self, sql):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
            self.close()
        except Exception as e:
            log.info("操作MySQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()
            self.close()


if __name__ == '__main__':
    order = MysqlDb("trade").select_db('select * from order_bill where trade_no = "10012024031511045516800007"')
    order_str = str(order)
    print(order_str[{'channel_fee'}])
    print(order_str.encode('utf-8'))
