import hashlib
import requests
from lib.base_utils import BaseUtils
from lib.config.sit import sit_config
from lib.config.pg import pg_config
from lib.config.la import la_config
from lib.config.ph import ph_config
from lib.config.id import id_config
from lib.config.th import th_config

class ApiRequester:
    def __init__(self):
        self.requests = requests.Session()
        self.requests.verify = False

    def construct_url(self, base_url, url, data):
        return f"{base_url}{url}?{data}sign={self.data['sign']}"

    def assert_code_equals(self, response, expected_code):
        assert response['code'] == expected_code, f"code码不是'{expected_code}', 实际值为: {response['code']}"

    def post_request(self, base_url, url, data, desc, expected_code='200'):
        full_url = self.construct_url(base_url, url, data)
        self.log.debug(f"{self.time.date_time_s()} 发起post请求:{desc}")
        self.log.debug(f"{self.time.date_time_s()} 请求时的入参: {full_url}")
        try:
            res = self.requests.post(full_url)
            res.raise_for_status()
            response_json = res.json()
            self.log.debug(f"接口返回值: {response_json}")
            if expected_code is not None:
                self.assert_code_equals(response_json, expected_code)
            return response_json
        except Exception as e:
            self.log.error(f"请求异常: {e}")
            raise

    def order_sign(self):
        keys = sorted(self.data)
        accsiiParams = ""
        orderNo = "TestOrderNo_" + self.time.get_timestamp()  # 测试订单号用时间戳生成
        self.data['orderNo'] = orderNo
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
        return accsiiParams

    def quest_sign(self):
        keys = sorted(self.data)
        accsiiParams = ""
        orderNo = "TestOrderNo_" + self.time.get_timestamp()  # 测试订单号用时间戳生成
        self.data['orderNo'] = orderNo
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
        return accsiiParams

    def get_md5(self, s):
        md = hashlib.md5()
        md.update(s.encode('utf-8'))
        sign = md.hexdigest()
        self.data["sign"] = sign
        return sign

    def post_id(self, url, data, desc, **kwargs):
        return self.post_request(id_config.base_url, url, data, desc, **kwargs)

    def post_test(self, url, data, desc, **kwargs):
        return self.post_request(sit_config.base_url, url, data, desc, **kwargs)

    def post_th(self, url, data, desc, **kwargs):
        return self.post_request(th_config.base_url, url, data, desc, **kwargs)

    def post_ph(self, url, data, desc, **kwargs):
        return self.post_request(ph_config.base_url, url, data, desc, **kwargs)

    def post_pg(self, url, data, desc, **kwargs):
        return self.post_request(pg_config.base_url, url, data, desc, **kwargs)

    def post_la(self, url, data, desc, **kwargs):
        return self.post_request(la_config.base_url, url, data, desc, **kwargs)

    def post_test_merchant_fail(self, url, data, desc, expected_code, **kwargs):
        return self.post_request(sit_config.base_url, url, data, desc, expected_code, **kwargs)
if __name__ == '__main__':
    pass