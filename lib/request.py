
from PIL import Image
import pytesseract
from io import BytesIO
import base64
import os
import json
import time
import requests
import time
import requests
from lib.settings.get_time import GetTime

class Auto_Login(GetTime):
    def __init__(self):

        self.session = requests.Session()
        self.timestamp = None  # 用于保存当前毫秒数
        self.dynamic_param = None

    def fetch_captcha_image(self):
        # 获取登录验证码
        self.timestamp = self.now_milliseconds()  # 保存当前毫秒数
        url = f'https://admintest-api.tikipay.co/gateway/sys/randomImage/{self.timestamp}?_t={self.get_timestamp_s()}&country=IDR&utc=0'
        response = self.session.get(url)

        if response.status_code != 200:
            print(f"GET 请求失败，状态码：{response.status_code}")
            return None

        try:
            # 解析响应内容为 JSON 格式
            data = response.json()

            # 从 JSON 数据中提取所需的字段
            desired_field = data.get('result')
            if not desired_field:
                print("未找到所需字段 'result'")
                return None

            desired_field = desired_field.split(",")[-1]
            image_data = Image.open(BytesIO(base64.b64decode(desired_field)))
            image_data.save("captcha_image.jpg")  # 保存图像
            print("图像已保存为:", os.path.join(os.getcwd(), "captcha_image.jpg"))
            return image_data

        except ValueError as e:
            print(f"无法解析响应内容为 JSON 格式: {e}")
            return None
        except Exception as e:
            print(f"处理异常时出错: {e}")
            return None

    def post_request(self,url, data):
        # 发送 POST 请求
        print("发送 POST 请求:")
        print("请求体:", json.dumps(data))  # 将数据转换为 JSON 格式字符串打印
        response = self.session.post(url, json=data)
        # 打印响应信息
        print("接收到的响应:")
        print("状态码:", response.status_code)
        print("响应头:", response.headers)
        print("响应体:", response.text)  # 打印响应内容
        # 返回响应内容
        return response.text

    def get_request(self, url, token):
        # 发送 GET 请求
        print("发送 GET 请求:")
        print("请求 URL:", url)

        # 设置请求头，添加 Authorization 字段
        headers = {'X-Access-Token': self.token}
        print(headers)

        # 发送 GET 请求，并传入请求头
        response = self.session.get(url, headers=headers)
        response_data = response.json()
        records = response_data.get("result", {}).get("records", [])

        # 提取 records 中每个元素的 channelCode 字段，并保存到列表中
        channel_codes = [record.get("channelCode") for record in records]
        print(channel_codes)
        # 打印响应信息
        print("接收到的响应:")
        print("状态码:", response.status_code)
        print("响应头:", response.headers)
        print("响应体:", response.text)  # 打印响应内容

        # 返回响应内容

        return channel_codes, response.text



    def perform_login(self):
        # 获取登录验证码进行登陆
        captcha_image = self.fetch_captcha_image()

        if captcha_image:
            # 识别验证码
            captcha_code = pytesseract.image_to_string(captcha_image).strip()
            print("识别到的验证码:", captcha_code)


            # 准备登录请求数据
            check_key = str(self.timestamp)  # 使用之前保存的毫秒数作为 check_key
            logo_url = ('https://admintest-api.tikipay.co/gateway/sys/login')
            login_data = {
                "username": "tikipay",
                "password": "Tikipay@123",
                "captcha": captcha_code,
                "checkKey": check_key,
            }

            # 发送登录请求
            login_response = self.post_request(logo_url,login_data)

            if login_response:
                print("登录成功:", login_response)
                # 保存token
                try:
                    self.token = json.loads(login_response)["result"]["token"]
                    print("Token 已保存:", self.token)
                except KeyError:
                    print("未找到token")
            else:
                print("登录失败")
        else:
            print("无法获取验证码")

    def xendit_pay_channel(self):
        # 先执行登录操作
        self.perform_login()
        time.sleep(2)

        if self.token:
            # 如果成功获取到 token，则可以使用它来发送请求
            url = f"https://admintest-api.tikipay.co/gateway/org.jeecg.modules.tikipay/payChannelInfo/list?_t={self.now_milliseconds()}&payChannelName=7&type=0&column=createTime&order=desc&field=id,,,channelCodeName,payChannelName,channelCodeRemote,type,payType,currency,status,createTime,updateTime,action&pageNo=1&pageSize=10&country=IDR&utc=0"

            # 发送请求
            request = self.get_request(url, token=self.token)
            return request
        else:
            print("未获取到 token，无法获取支付通道信息")
            return None


# 使用示例
if __name__ == "__main__":
    # Auto_Login().post_request()
    # Auto_Login().perform_login(
    Auto_Login().xendit_pay_channel()

