import requests
from lib.base_utils import BaseUtils
from lib.utils.config.sit import sit_config
from lib.utils.config.pg import pg_config
from lib.utils.config.la import la_config
from lib.utils.config.ph import ph_config
from lib.utils.config.id import id_config
from lib.utils.config.th import th_config
import json

class Payout(BaseUtils):
    def setup(self, data, privateKey):
        self.data = data
        self.privateKey = privateKey
        self.requests = requests.Session()
        self.requests.verify = False

        try:
            with open('D://Tiki/lib/utils/config/proxy.json', 'r') as file:
                self.proxies = json.load(file)
            self.requests.proxies = self.proxies
        except FileNotFoundError:
            self.requests.proxies = {}  # 如果文件未找到，则不使用代理



    def send_post_request(self, base_url, url, desc):
        self.data["sign"] = self.sign.sign1(self.data, self.privateKey)
        data = self.sign.generate_params(self.data)
        full_url = f"{base_url}{url}?{data}&sign={self.data['sign']}"
        self.log.debug(f"{self.time.date_time_s()} 请求url: {base_url}{url}")
        self.log.debug(f"{self.time.date_time_s()} 发起post请求:{desc}")
        self.log.debug(f"{self.time.date_time_s()} 请求时的入参: {data}")

        try:
            res = self.requests.post(full_url, proxies=self.proxies)
            print(res)
            res.raise_for_status()
            response_json = res.json()
            self.log.debug(f"接口返回值: {response_json}")
            return response_json
        except Exception as e:
            self.log.error(f"请求异常: {e}")
            raise


    def post(self, env, url, desc):
        config = {
            "sit": sit_config.base_url,
            "pg": pg_config.base_url,
            "la": la_config.base_url,
            "id": id_config.base_url,
            "th": th_config.base_url,
            "ph": ph_config.base_url
        }
        base_url = config.get(env)
        if base_url is None:
            raise ValueError(f"未知的环境: {env}")
        return self.send_post_request(base_url, url, desc)


if __name__ == '__main__':
    # 示例用法
    pass