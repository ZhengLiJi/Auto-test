
import requests
from lib.base_utils import BaseUtils
from lib.config.sit import sit_config
from lib.config.pg import pg_config
from lib.config.la import la_config
from lib.config.ph import ph_config
from lib.config.id import id_config
from lib.config.th import th_config
from datetime import datetime

class Payout(BaseUtils):
    def setup(self, data, privateKey):
        self.data = data
        self.privateKey = privateKey
        self.requests = requests.Session()
        self.requests.verify = False

    def send_post_request(self, base_url, url, desc):
        self.data["sign"] = self.sign.sign1(self.data, self.privateKey)
        data = self.sign.generate_params(self.data)
        full_url = f"{base_url}{url}?{data}&sign={self.data['sign']}"
        self.log.debug(f"{self.time.date_time_s()} 请求url: {base_url}{url}")
        self.log.debug(f"{self.time.date_time_s()} 发起post请求:{desc}")
        self.log.debug(f"{self.time.date_time_s()} 请求时的入参: {data}")

        try:
            res = self.requests.post(full_url)
            res.raise_for_status()
            response_json = res.json()
            self.log.debug(f"接口返回值: {response_json}")
            return response_json
        except Exception as e:
            self.log.error(f"请求异常: {e}")
            raise

    def post_sit(self, url, desc):
        return self.send_post_request(sit_config.base_url, url, desc)

    def post_pg(self, url, desc):
        return self.send_post_request(pg_config.base_url, url, desc)

    def post_la(self, url, desc):
        return self.send_post_request(la_config.base_url, url, desc)

    def post_id(self, url, desc):
        return self.send_post_request(id_config.base_url, url, desc)

    def post_th(self, url, desc):
        return self.send_post_request(th_config.base_url, url, desc)

    def post_ph(self, url, desc):
        return self.send_post_request(ph_config.base_url, url, desc)

if __name__ == '__main__':
    pass