#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/11 15:29
# @Author  : zheng
# @File    : payout_method.py
# @Software: PyCharm


class PayoutMethod:

    @staticmethod
    def choose_quarter(q):
        quarter = {
            "1": "_q1",
            "2": "_q1",
            "3": "_q1",
            "4": "_q2",
            "5": "_q2",
            "6": "_q2",
            "7": "_q3",
            "8": "_q3",
            "9": "_q3",
            "10": "_q4",
            "11": "_q4",
            "12": "_q4",
        }
        return quarter[q]





