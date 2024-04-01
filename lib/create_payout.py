
import requests

from api.trade import Trade
from lib.utils.base_utils import BaseUtils
from lib.config.sit import sit_config
from lib.config.pg import pg_config
from lib.config.la import la_config
from lib.config.ph import ph_config
from lib.config.id import id_config
from lib.config.th import th_config
from lib.utils.requests import Requests


class Payout():
    # def setup(self, data, privateKey):
    #     self.data = data
    #     self.privateKey = privateKey
    #     self.requests = requests.Session()
    #     self.requests.verify = False

    def __int__(self):
        self.trade = Trade()
        self.user = User()

    def send_post_request(self, base_url, url, desc):
        self.user.login()
        self.data["sign"] = self.sign.sign1(self.data, self.privateKey)
        data = self.sign.generate_params(self.data)
        full_url = f"{base_url}{url}?{data}&sign={self.data['sign']}"
        self.log.debug(f"{self.time.date_time_s()} 请求url: {base_url}{url}")
        self.log.debug(f"{self.time.date_time_s()} 发起post请求:{desc}")
        self.log.debug(f"{self.time.date_time_s()} 请求时的入参: {data}")
        res = self.trade.payout(base_url, data)
        res.raise_for_status()
        self.trade.refund()
        response_json = res.json()
        self.trade.log.debug(f"接口返回值: {response_json}")
        self.trade.delete()
        return response_json


if __name__ == '__main__':
    pass