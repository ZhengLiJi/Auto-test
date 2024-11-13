#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/15 11:35
# @Author  : zheng
# @File    : order_method.py
# @Software: PyCharm
from case_data.api_data.pay_channel import *


class OrderMethod:

    @staticmethod
    def assert_payment_link_present(pay_channel, pay_code):
        """
        根据指定的支付渠道，断言至少一个预期链接存在于结果的“payCode”中。
        """

        assertions = {
            dana: lambda code: any(link in code for link in ([dana_link] if isinstance(dana_link, str) else dana_link) +
                                   ([test_link] if isinstance(test_link, str) else test_link)),
            shopeepay: lambda code: shopeepay_link in code,
            qris: lambda code: True,  # 这里可以添加相应的断言逻辑
        }
        # 合并相同的断言逻辑
        digit_only_channels = {bni, permata, bca, cimb, mandiri, bri}
        for channel in digit_only_channels:
            assertions[channel] = lambda code: code.isdigit()

        # 获取对应支付渠道的断言逻辑
        assertion = assertions.get(pay_channel)

        if assertion is None:
            raise ValueError(f"未知的支付渠道: {pay_channel}")

        assertion_result = assertion(pay_code)

        if not assertion_result:
            raise AssertionError(f"没有返回{pay_channel}支付方式的预期链接或支付代码格式不正确")

        return assertion_result

if __name__ == '__main__':
    pay = OrderMethod.assert_payment_link_present('17', 'https://link.dana.id')
    print(pay)
