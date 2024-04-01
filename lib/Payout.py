
import requests
from lib.utils.base_utils import BaseUtils
from lib.config.sit import sit_config
from lib.config.pg import pg_config
from lib.config.la import la_config
from lib.config.ph import ph_config
from lib.config.id import id_config
from lib.config.th import th_config
from lib.utils.requests import Requests
# http://www.baidu.com/payout/get_user_info
# http://www.baidu.com/payout/delete_user

class Payout(Requests):
    def send_post_request(self, base_url, url, desc, data, privateKey):
        url = "send_post_request"
        self.data["sign"] = self.sign.sign1(self.data, self.privateKey, data['privateKey'])
        data = self.sign.generate_params(self.data)
        full_url = f"{base_url}{url}?{data}&sign={self.data['sign']}"
        self.log.debug(f"{self.time.date_time_s()} 请求url: {base_url}{url}")
        self.log.debug(f"{self.time.date_time_s()} 发起post请求:{desc}")
        self.log.debug(f"{self.time.date_time_s()} 请求时的入参: {data}")
        res = self.post(full_url)
        res.raise_for_status()
        response_json = res.json()
        self.log.debug(f"接口返回值: {response_json}")
        return response_json

    def get_user_info(self, base_url, url, desc, data, privateKey):
        url = "get_user_info"
        self.data["sign"] = self.sign.sign1(self.data, self.privateKey, data['privateKey'])
        data = self.sign.generate_params(self.data)
        full_url = f"{base_url}{url}?{data}&sign={self.data['sign']}"
        res = self.post(full_url)
        res.raise_for_status()
        response_json = res.json()
        self.log.debug(f"接口返回值: {response_json}")
        return response_json


class TestCaseA():
    def setup(self):
        self.create_payout = create_payout()
        self.delete_payout = delete_payout()
        "================================"
        self.payout = Payout()

    def logic(self):
        self.payout.create()
        ...
        self.payout.delete()
if __name__ == '__main__':
    pass