#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/11 18:27
# @Author  : zheng
# @File    : client_base.py
# @Software: PyCharm
from lib.core.client.payout_method import PayoutMethod
from lib.core.client.order_method import OrderMethod
from lib.core.client.collection_scene import CollectionScene
from lib.core.client.sql import Sql
class ClientBase:
    _have = {}

    @property
    def payout_method(self):
        if self._have.get("payout_method") is None:
            self._have["payout_method"] = PayoutMethod()
        return self._have["payout_method"]

    @property
    def order_method(self):
        if self._have.get('order_method') is None:
            self._have["order_method"] = OrderMethod()
        return self._have["order_method"]

    @property
    def collection_scene(self):
        if self._have.get('collection_scene') is None:
            self._have['collection_scene'] = CollectionScene()
        return self._have['collection_scene']

    @property
    def sql(self):
        if self._have.get('sql') is None:
            self._have['sql'] = Sql()
        return self._have['sql']


if __name__ == '__main__':
    pass


