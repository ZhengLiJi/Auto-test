#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/8 11:15
# @Author  : zheng
# @File    : mysql.py
# @Software: PyCharm
import pymysql
from lib.utils.database.base_mysql import BaseSQL
from lib.utils.config.sit import sit_config


class MySQL(BaseSQL):
    def __init__(self, db, host=sit_config.mysql_host, port=sit_config.mysql_port, user=sit_config.mysql_user, password=sit_config.mysql_password):
        super(MySQL, self).__init__(db, host, port, user, password)

    def connect(self):
        db = pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password,
                             db=self.database)
        return db



