from selenium import webdriver
from PIL import Image
import pytesseract
from io import BytesIO
import base64
import os
import json
import time
import requests
# 这一段就不需要了 直接接口拿 转jpeg 放到ocr中识别
import time
import requests
from lib.settings.get_time import GetTime

class Auto_Login(GetTime):
    def __init__(self):
        self.session = requests.Session()
        self.timestamp = None  # 用于保存当前毫秒数

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

    def post_request(self, data):
        # 发送 POST 请求
        print("发送 POST 请求:")

        print("请求体:", json.dumps(data))  # 将数据转换为 JSON 格式字符串打印

        # 发送 POST 请求
        url = "https://admintest-api.tikipay.co/gateway/sys/login"

        # 发送 POST 请求
        response = self.session.post(url, json=data)

        # 打印响应信息
        print("接收到的响应:")
        print("状态码:", response.status_code)
        print("响应头:", response.headers)
        print("响应体:", response.text)  # 打印响应内容

        # 返回响应内容
        return response.text

    def perform_login(self):
        # 获取登录验证码
        captcha_image = self.fetch_captcha_image()

        if captcha_image:
            # 识别验证码
            captcha_code = pytesseract.image_to_string(captcha_image).strip()
            print("识别到的验证码:", captcha_code)

            # 准备登录请求数据
            check_key = str(self.timestamp)  # 使用之前保存的毫秒数作为 check_key
            login_data = {
                "username": "tikipay",
                "password": "Tikipay@123",
                "captcha": captcha_code,
                "checkKey": check_key,
            }

            # 发送登录请求
            login_response = self.post_request(login_data)

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

# 使用示例
if __name__ == "__main__":
    Auto_Login().perform_login()
