import allure
import pytest

from lib.create_order2 import CreateOrder
from case_data.idr_data import xendit1_data

# 你的Test_create_order就是父类 case层不应该加上api的请求逻辑和参数拼接， 需要的是直接把参数给接口，然后拿返回，再判断你这次组装的 {符合你业务的数据} 【返回的结果】是否符合你的 [预期值]
# 比如你的ovo_success 你的业务数据 = '100119', '2023', "IDR", '20110', '081382826304', '15', '97fa79f073c7c5e3c97b00b50b156eaa' 返回的结果就是result assert就是把实际结果和你的预期进行判断
class TestFaspay(CreateOrder):
    # 这个create_order应该是父类去实现
    # def createOrder(self, merchantId="", productId="", currency="", amount="", payerPhone="", payChannel="",
    #                 privateKey=''):
    #     url = "/pay/createOrder"
    #     accsiiParams = self.order_sign()
    #     sign = self.get_md5(accsiiParams)
    #     return self.post_id(url, self.data['params'], '下单', )

    # 省略的写法
    # @allure.title("监控xendit通道各支付方式是否维护")
    @pytest.mark.parametrize("data", xendit1_data)# 如果 你觉得这样写数据很丑
    def test_fas_pay(self, data):
        result = self.create_order(data['data'])
        print(result)
        assert result == data['result']


if __name__ == '__main__':
    TestFaspay.create_order()



