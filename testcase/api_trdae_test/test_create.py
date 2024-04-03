import allure
import os
from api.trade import Trade
from common.mysql import MysqlDb
from lib.settings.logger import log
from lib.settings.get_time import GetTime
from case_data.api_data.idr_data import *
from case_data.api_data.order_data import *
import ast
import pytest
# from create_order_file import CreateOrder

@allure.epic("针对trade单元测试")
@allure.feature("下单接口")
class TestCreate:
    def setup_class(self):
        self.xxx = Trade()
        self.log = log
        self.time = GetTime()
        self.mysql = MysqlDb('trade')

    def perform_order_test(self, data, privateKey, expected_code=None, expected_msg=None, expected_type=None, orderNo=None,
                           merchant_fee=None,channel_fee=None, pay_channel=None):
        if orderNo is not None and 'orderNo' not in data:
            # 如果 orderNo 存在且 data 中没有 orderNo 字段，则将 orderNo 添加到 data 中
            data['orderNo'] = orderNo
        elif 'orderNo' not in data:
            data['orderNo'] = 'TestOrderNo_' + self.time.get_timestamp()

        self.log.info(f"{self.time.date_time_s()} *************** 开始执行用例 ***************")
        result = self.xxx.create(data, privateKey)

        if pay_channel is not None or merchant_fee is not None:
            # 如果传入了 pay_channel 或 fee_rate，则要断言是否返回 200
            try:
                assert result.get('code') == '200', "预期状态码为 200，实际状态码为 {}".format(result.get('code'))
            except AssertionError as e:
                raise AssertionError(f"{e}")

            if pay_channel is not None:
                if data["payChannel"] == dana:
                    # 断言链接是否包含"dana"
                    assert dana_link in result.get('payCode') or \
                           dana_link2 in result.get('payCode') or \
                           test_link in result.get('payCode'), "没有返回dana支付方式的链接"
                elif data["payChannel"] == shopeepay:
                    assert shopeepay_link in result.get('payCode'), "没有返回shopeepay支付方式的链接"

                # elif pay_code == qris:
                #     pass

                elif data["payChannel"] in [bni, permata, bca, cimb, mandiri, bri]:
                    # 断言支付代码是否全为数字
                    assert result.get('payCode').isdigit(), "支付代码不全为数字"

            # 查询订单数据
            order_data = self.mysql.select_db(f"select * from order_bill where order_no = '{result.get('orderNo')}'")
            assert order_data, f"数据库中未找到订单号为 {data('orderNo')} 的记录"

            if pay_channel is not None:
                assert order_data[0]['pay_channel'] == pay_channel, f"支付渠道不符合预期，实际值为 {order_data[0]['pay_channel']}"
                # 如果传入了 pay_channel，则断言支付渠道,路由场景。


            if merchant_fee is not None:
                # 如果传入了 merchant_fee，则断言费率，费率场景，查看商户费率是否正常扣除
                try:
                    assert order_data[0][
                           'merchant_fee'] == merchant_fee, f"费率不符合预期，实际值为 {order_data[0]['merchant_fee']}" #普通的商户费率
                except AssertionError as e:
                    raise AssertionError(f"{e}")

                if channel_fee is not None:
                    assert order_data[0][
                               'channel_fee'] == channel_fee, f"费率不符合预期，实际值为 {order_data[0]['channel_fee']}"  #渠道费率


        else:
            # 如果 pay_channel 和 merchant_fee 都没有传入，则默认执行状态码和消息类型的断言
            try:
                assert result.get('code') == expected_code and (
                        (expected_msg and result.get('msg') == expected_msg) or
                        (expected_type and result.get('type') == expected_type)
                ), (
                    f"断言失败: 实际结果为 {result.get('code')},{result.get('msg') or result.get('type')} "
                    f"期望结果为 {expected_code}. {expected_msg or expected_type}"
                )
            except AssertionError as e:
                raise AssertionError(f"{e}")

        self.log.info(f"{self.time.date_time_s()} *************** 执行用例结束 ***************")

    @allure.story('费率场景')
    @pytest.mark.parametrize("data, privateKey,merchant_fee,channel_fee, title", rate_case)
    def test_rate_case(self, data, privateKey, merchant_fee, channel_fee, title):
        allure.dynamic.title(f"{title}")
        self.perform_order_test(data, privateKey, merchant_fee=merchant_fee, channel_fee=channel_fee)

    @allure.story('路由用户标识')
    @pytest.mark.parametrize("data, privateKey, paychannel_code, title", user_routing)
    def test_user_routing(self, data, privateKey, paychannel_code, title):
        allure.dynamic.title(f"{title}")
        self.perform_order_test(data, privateKey, pay_channel=paychannel_code)

    @allure.story('路由金额区间')
    @pytest.mark.parametrize("data, privateKey,paychannel_code, title", amount_routing)
    def test_amount_routing(self, data, privateKey, paychannel_code, title):
        allure.dynamic.title(f"{title}")
        self.perform_order_test(data, privateKey, pay_channel=paychannel_code)

    @allure.story('普通路由场景')
    @pytest.mark.parametrize("data, privateKey, paychannel_code, title", normal_routing)
    def test_normal_routing(self, data, privateKey, paychannel_code, title):
        allure.dynamic.title(f"{title}")
        self.perform_order_test(data, privateKey, pay_channel=paychannel_code)


    @allure.story("下单接口异常case合计")
    @pytest.mark.parametrize("data, privateKey, expected_code, expected_msg, title", create_order_data)
    @pytest.mark.xfail     #断言失败则跳过
    def test_createorder_error(self,data, privateKey, expected_code, expected_msg, title):
            allure.dynamic.title(f"{title}")
            response = self.perform_order_test(data, privateKey, expected_code=expected_code, expected_msg=expected_msg)
            print(response)

    @allure.story("限额场景")
    @pytest.mark.parametrize("data, privateKey, expected_code, expected_msg, title", amount_lmiti)
    @pytest.mark.xfail     #断言失败则跳过
    def test_amount_lmiti(self,data, privateKey, expected_code, expected_msg, title):
            allure.dynamic.title(f"{title}")
            response = self.perform_order_test(data, privateKey, expected_code=expected_code, expected_msg=expected_msg)
            print(response)


if __name__ == '__main__':
    if os.path.exists("D:/Tiki/results"):
        os.system("rm -r D:/Tiki/results")

    pytest.main(["-vs", '--alluredir', 'D:/Tiki/results'])

    # 生成allure报告
    os.system("allure generate D:/Tiki/results -o D:/Tiki/reports --clean")