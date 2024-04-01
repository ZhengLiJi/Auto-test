#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/30 17:35
# @Author  : zheng
# @File    : requests.py
# @Software: PyCharm
import requests

from lib.utils.base_utils import BaseUtils


class Requests(BaseUtils):
    def __init__(self):
        """

        :param base_url:  域名
        :param api: api接口路徑
        :param data: 傳參
        :param desc: 描述
        """
        self.request = requests.session()
        self.request.verify = False

    def save_request_after_log(self, url, data, desc, methods, base_url="http://www.baidu.com"):
        self.log.debug(f"{self.time.date_time_s()} 请求url: {base_url}{url}")
        self.log.debug(f"{self.time.date_time_s()} 发起{methods}请求:{desc}")
        self.log.debug(f"{self.time.date_time_s()} 请求时的入参: {data}")

    def save_request_before_log(self, response):
        self.log.debug(f"{self.time.date_time_s} 返回的結果：")
        self.log.debug(f"{self.time.date_time_s} status_code：")

    def post(self, url, data, desc, base_url="http://www.baidu.com"):
        self.save_request_after_log()
        self.request.post(base_url+url, json=data)
        self.save_request_before_log()


    def get(self, url, data, desc, base_url="http://www.baidu.com"):
        pass

    def put(self, url, data, desc, base_url="http://www.baidu.com"):
        pass

    def delete(self, url, data, desc, base_url="http://www.baidu.com"):
        pass
