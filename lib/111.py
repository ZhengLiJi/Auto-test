#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
import requests
# class FooParent(object):
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print('Parent')
#
#     def bar(self, message):
#         print("%s from Parent" % message)
#
#
# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
#         super(FooChild, self).__init__()
#         print('Child')
#
#     def bar(self, message):
#         super(FooChild, self).bar(message)
#         print('Child bar fuction')
#         print(self.parent)
#
#
# if __name__ == '__main__':
#     # FooParent()
#     # FooParent().bar(1)
#     fooChild = FooChild()
#     fooChild.bar('HelloWorld')


def post2(self, url, data, desc, **kwargs):
    self.log.debug(f"{self.time.date_time_s()} 发起post请求:{desc}")
    self.log.debug(f"{self.time.date_time_s()} 请求时的入参: {url + '?' + data + 'sign=' + self.data['sign']}")
    res = self.requests.post( url + '?' + data + 'sign=' + self.data["sign"])
    print(res)
    assert res.status_code == 200, f"响应码不为200, {res.json()}"
    self.log.debug(f"{self.time.date_time_s()} 接口返回值: {res.json()}")
    return res.json()

post2('1','www','777','1')
