from abc import abstractmethod

import pandas as pd

from lib.utils.settings.logger import log


class BaseSQL(object):
    __instance = {}
    __db = None
    __cursor = None

    def __new__(cls, *args, **kwargs):
        """
        单例模式，如果传入的参数相同，则不创建新的对象；防止内存过大
        Args:
            *args:
            **kwargs:
        """
        key = args[0]
        if key not in cls.__instance:
            cls.__instance[key] = super().__new__(cls)
        return cls.__instance[key]

    def __init__(self, db, host, port, user, password):
        self.host = host
        self.port = port
        self.database = db.database
        self.username = user
        self.password = password

    @property
    def db(self):
        if not self.__db:
            self.__db = self.connect()
        return self.__db

    @property
    def cursor(self):
        if not self.__cursor:
            self.__cursor = self.db.cursor()
        return self.__cursor

    @abstractmethod
    def connect(self):
        """数据库驱动引擎"""
        pass

    def execute(self, sql):
        """执行命令
        sql: sql语句
        """
        log.info(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            log.error(e.args)
            if "Lost connectsion" in str(e.args):
                log.warning(f"数据库断开，尝试重新连接")
                self.__db = self.connect()
            self.db.rollback()

    @abstractmethod
    def insert(self, table, **data):
        """增"""

        sql = "insert into {table} ("
        for k in data.keys():
            sql += f"`{k}`, "
        sql = sql[:-2] + ") values ("
        for k in data.values():
            if isinstance(k, (int, float)):
                sql += f"{k}"
            else:
                sql += f"`{k}`"
        sql = sql[:-2] + ');'
        self.execute(sql)

    def delete(self, sql):
        """删"""
        self.execute(sql)


    def update(self, table, condition, **data):
        """改"""
        sql = f'''UPDATE {table} SET '''
        for k, v in data.items():
            if isinstance(v, int) or isinstance(v, float):
                sql += f'{k} = {v}, '
            else:
                sql += f"{k} = '{v}', "
        sql = f"{sql[:-2]} WHERE {condition};"
        self.execute(sql)

    def search(self, sql):
        """执行查询并返回结果"""
        self.execute(sql)
        result = self.cursor.fetchall()
        columns = [col[0] for col in self.cursor.description]
        data = []
        for row in result:
            item = {}
            for idx, value in enumerate(row):
                item[columns[idx]] = value
            data.append(item)
        return data

    def search_one(self, sql, column):
        """获取某个值"""
        info = self.search(sql)
        value = info[column][0]
        log.info(f"{column}: {value}")
        return str(value)

    def clear_table(self, table):
        """清空表数据，慎用"""
        log.info(f"正在清空数据表: {table}")
        sql = f"truncate table {table}"
        self.execute(sql)

    def search_one_by_range(self, sql, columu, range):
        """根据指定行号获取某个值"""
        info = self.search(sql)
        if info.empty:
            return ""
        else:
            value = str(info[columu][range])
            log.info(f"{columu}: {value}")
            return value

    def close(self):
        """关闭数据库连接"""
        self.db.close()
        self.__db = None
        self.__cursor = None

    def __del__(self):
        if self.__db:
            self.close()


if __name__ == '__main__':
    pass
