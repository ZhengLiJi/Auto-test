import hashlib
import requests

from lib.base_utils import BaseUtils
from lib.config.sit import sit_config
from lib.config.pg import pg_config
from lib.config.la import la_config
from lib.config.ph import ph_config
from lib.config.id import id_config
from lib.config.th import th_config
from functools import lru_cache
import pytest
# 两边的类名取反了。 这里才是api了。
# 你另外一边继承的class， 才是TestCase了。 命名规则你需要修改
# 文件名也错了， 用例文件名需要test_开头或者_test结尾

class CreateOrder(BaseUtils):
# class CreateOrder(BaseUtils):

    def setup(self, merchantId, productId, currency, amount, payerPhone, payChannel, privateKey):
        self.data = {
            'version': 1.0,
            'merchantId': merchantId,
            'productId': productId,
            'currency': currency,
            'orderNo': '',
            'amount': amount,
            'payChannel': payChannel,
            'expectPayCodeType': 0,
            'subject': 'TestSubject',
            'payerName': 'test',
            'payerPhone': payerPhone,
            'sign': "sign",
            "params": "params"
        }

        self.privateKey = privateKey

        #
        self.requests = requests.Session()  # 长链接
        self.requests.verify = False

    def construct_url(self, base_url, url, data):
        return f"{base_url}{url}?{data}sign={self.data['sign']}"

    def assert_code_equals(self, response, expected_code):

        assert response['code'] == expected_code, f"code码不是'{expected_code}', 实际值为: {response['code']}"

    def post_request(self, base_url, url, data, desc, expected_code = '200'):
        full_url = self.construct_url(base_url, url, data)
        self.log.debug(f"{self.time.date_time_s()} 发起post请求:{desc}")
        self.log.debug(f"{self.time.date_time_s()} 请求时的入参: {full_url}")
        try:
            res = self.requests.post(full_url)
            res.raise_for_status()
            response_json = res.json()
            self.log.debug(f"接口返回值: {response_json}")
            if expected_code is not None:
                self.assert_code_equals(response_json,expected_code)
            return response_json
        except Exception as e:
            self.log.error(f"请求异常: {e}")
            raise

    def order_sign(self):
        keys = sorted(self.data)
        """sorted按照ASCLL从小到大排序"""

        accsiiParams = ""
        orderNo = "TestOrderNo_" + self.time.get_timestamp()  # 测试订单号用时间戳生成
        self.data['orderNo'] = orderNo

        # print(orderNo)
        for i in keys:
            if i == "orderNo":
                accsiiParams = accsiiParams + i + "=" + self.data[i]
            elif i == "merchantId":
                accsiiParams = accsiiParams + i + "=" + str(self.data[i])
            elif i == "productId":
                accsiiParams = accsiiParams + i + "=" + str(self.data[i])
            elif i == "currency":
                accsiiParams = accsiiParams + i + "=" + str(self.data[i])
            elif i != "sign" and i != "params":
                accsiiParams = accsiiParams + i + "=" + str(self.data[i])

            if i != "sign" and i != "params":
                accsiiParams = accsiiParams + '&'

            elif i != "sign":
                accsiiParams = accsiiParams
                self.data['orderNo'] = orderNo

        self.data["params"] = accsiiParams
        accsiiParams = accsiiParams[0:len(accsiiParams) - 1] + self.privateKey
        # print(accsiiParams)
        return accsiiParams

    def get_md5(self, s):
        md = hashlib.md5()
        md.update(s.encode('utf-8'))
        sign = md.hexdigest()
        self.data["sign"] = sign
        return sign

        # '''拼接加密参数，sign本身不参与签名'''

    def post_id(self, url, data, desc, **kwargs):
        return self.post_request(id_config.base_url, url, data, desc)

    def post_dtest(self, url, data, desc, **kwargs):
        return self.post_request(sit_config.base_url, url, data, desc)

    def post_th(self, url, data, desc, **kwargs):
        return self.post_request(th_config.base_url, url, data, desc)

    def post_ph(self, url, data, desc, **kwargs):
        return self.post_request(ph_config.base_url, url, data, desc)

    def post_pg(self, url, data, desc, **kwargs):
        return self.post_request(pg_config.base_url, url, data, desc)

    def post_la(self, url, data, desc, **kwargs):
        return self.post_request(la_config.base_url, url, data, desc)

    def post_test_merchant_fail(self, url, data, desc,expected_code):
        return self.post_request(sit_config.base_url, url, data, desc,expected_code)


    def create_order(self, merchant_id, product_id, currency, amount, phone_number, pay_channel,
                     private_key):
        data = CreateOrder()
        data.setup(merchant_id, product_id, currency, amount, phone_number, pay_channel, private_key)
        accsiiParams = data.order_sign()
        sign = data.get_md5(accsiiParams)
        url = '/pay/createOrder'
        # 发起请求
        res = data.post_dtest(url=url, data=data.data['params'],
                              desc='模拟xendit dana下单成功', expected_code='200')
        return res


if __name__ == '__main__':
    '''1表示通道回调成功，2表示通道失败'''
    xendit_dana_2 = CreateOrder()
    # xendit_dana_1 = Test_create_order(100119, 2023, "IDR", 10000, '081382826301', 17,
    #                                   '97fa79f073c7c5e3c97b00b50b156eaa')

    xendit_dana_2.setup(100119, 2023, "IDR", 10000, '081382826301', 17,
                                      '97fa79f073c7c5e3c97b00b50b156eaa')
    accsiiParams = xendit_dana_2.order_sign()
    sign = xendit_dana_2.get_md5(accsiiParams)
    # resp = xendit_dana_1.post_th(url="/pay/createOrder", data=xendit_dana_1.data['params'],
                                 # desc='模拟xendit dana下单回调成功', expected_code=200)
    #
    # 指定预期状态码为 88012
    resp = xendit_dana_2.post_test_merchant_fail(url="/pay/createOrder", data=xendit_dana_2.data['params'],
                                 desc='模拟xendit dana下单回调成功' ,expected_code = '88012')

    print(resp)











