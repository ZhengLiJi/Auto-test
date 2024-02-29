import hashlib
import requests
from lib.base_utils import BaseUtils
from lib.config.sit import sit_config
from functools import lru_cache

class Xixi(BaseUtils):

    def __init__(self,merchantId,productId ,currency,amount , payerPhone ,payChannel,privateKey):
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

        # elif merchantId == 100170:
        #     self.privateKey = '300a1baf3fe8de94b406ff64ef56c5e9'
        # elif merchantId == 100171:
        #     self.privateKey = '735fa9dc2af4e1792d34d91ddb18ea69'



        #
        self.requests = requests.Session() # 长链接
        self.requests.verify = False



    def order_sign(self):
        keys = sorted(self.data)
        """sorted按照ASCLL从小到大排序"""

        accsiiParams = ""
        orderNo = "TestOrderNo_" +  self.time.get_timestamp()#测试订单号用时间戳生成
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
        accsiiParams = accsiiParams[0:len(accsiiParams)-1] +  self.privateKey
        # print(accsiiParams)
        return accsiiParams




    def get_md5(self,s):
        md = hashlib.md5()
        md.update(s.encode('utf-8'))
        sign = md.hexdigest()
        self.data["sign"] = sign
        return sign

        # '''拼接加密参数，sign本身不参与签名'''

    def assert_code_equals(self,response, expected_code):
        """
        断言返回的 JSON 数据中的 code 字段是否等于期望的值。

        Args:
            response (dict): 包含响应 JSON 数据的字典。
            expected_code (str): 期望的 code 字段值。

        Raises:
            AssertionError: 如果 code 字段值不等于期望的值，则触发 AssertionError。
        """
        assert response['code'] == expected_code, f"code码不是'{expected_code}', 实际值为: {response['code']}"

    # 调用示例：

    def post(self, url, data, desc, **kwargs):

        self.log.debug(f"{self.time.date_time_s()} 发起post请求:{desc}")

        self.log.debug(f"{self.time.date_time_s()} 请求时的入参: {url +'?' + data + 'sign=' + self.data['sign']}")
        res = self.requests.post(sit_config.base_url + url + '?' + data +  'sign=' + self.data["sign"])
        # verify = False
        print(res)
        # assert res.status_code == 200, f"响应码不为200, {res.json()}"
        # self.log.debug(f"{self.time.date_time_s()} 接口返回值: {res.json()}")
        self.assert_code_equals(res.json(), '200')  # 调用 assert_code_equals 方法
        self.log.debug(f"{self.time.date_time_s()} 接口返回值: {res.json()}")
        return res.json()






    def post2(self, url, data, desc, **kwargs):

        self.log.debug(f"{self.time.date_time_s()} 发起post请求:{desc}")
        self.log.debug(f"{self.time.date_time_s()} 请求时的入参: {url +'?' + data + 'sign=' + self.data['sign']}")
        res = self.requests.post(sit_config.base_url + url + '?' + data +  'sign=' + self.data["sign"])
        print(res)
        assert res.status_code == 200, f"响应码不为200, {res.json()}"
        self.log.debug(f"{self.time.date_time_s()} 接口返回值: {res.json()}")
        return res.json()


if __name__ == '__main__':

    '''1表示通道回调成功，2表示通道失败'''
    xendit_dana_1 = Xixi(1001191,2023, "IDR", 10000, '081382826301', 17,'97fa79f073c7c5e3c97b00b50b156eaa')

    # # xendit_dana_2 = Xixi(100119, 2023, 'IDR', '20101', '081382826301', '17', '97fa79f073c7c5e3c97b00b50b156eaa')
    accsiiParams = xendit_dana_1.order_sign()
    sign = xendit_dana_1.get_md5(accsiiParams)
    resp = xendit_dana_1.post(url = "/pay/createOrder" , data=xendit_dana_1.data['params'], desc='模拟xendit dana下单回调成功')













