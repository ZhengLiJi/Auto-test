import allure
import os
from case_data.api_data.order_data import *
import pytest
# from create_order_file import CreateOrder
from testcase.payout.create import Create
import time
@allure.epic("针对trade单元测试")
@allure.feature("下单接口")
class TestCreate:
    def get_current_env(self):
            return os.environ.get('env')

    def skip_if_env_not_match(self, test_env):
        current_env = self.get_current_env()
        if test_env != current_env:
            pytest.skip(
                f"Skipping test because current environment '{current_env}' does not match test environment '"
                f"{test_env}'"
            )

    # @allure.story('费率场景')
    # @pytest.mark.parametrize("data, env, privateKey, merchant_fee, channel_fee, title", rate_case)
    # def test_rate_case(self, data, env, privateKey, merchant_fee, channel_fee, title):
    #
    #     allure.dynamic.title(f"{title}")
    #     self.skip_if_env_not_match()



    @allure.story('路由用户标识')
    @pytest.mark.parametrize("data, env, privateKey, paychannel_code, title", user_routing)
    def test_user_routing(self, data, env, privateKey, paychannel_code, title):
        allure.dynamic.title(f"{title}")
        self.skip_if_env_not_match(env)
        # 打印参数化数据的值
        print(
            f"Running test with data: {data}, env: {env}, privateKey: {privateKey}, paychannel_code: "
            f"{paychannel_code}, title: {title}")
        # 调用 perform_order() 方法
        Create().perform_order(env, data, privateKey, pay_channel=paychannel_code)

    @allure.story('路由金额区间')
    @pytest.mark.parametrize("data, env, privateKey, paychannel_code, title", amount_routing)
    def test_amount_routing(self, data, env, privateKey, paychannel_code, title):
        allure.dynamic.title(f"{title}")
        self.skip_if_env_not_match(env)
        # 打印参数化数据的值
        print(
            f"Running test with data: {data}, env: {env}, privateKey: {privateKey}, paychannel_code: "
            f"{paychannel_code}, title: {title}")
        # 调用 perform_order() 方法
        Create().perform_order(env, data, privateKey, pay_channel=paychannel_code)

    @allure.story('普通路由场景')
    @pytest.mark.parametrize("data, env, privateKey, paychannel_code, title", normal_routing)
    def test_normal_routing(self, data, env, privateKey, paychannel_code, title):
        allure.dynamic.title(f"{title}")
        self.skip_if_env_not_match(env)
        # 打印参数化数据的值
        print(
            f"Running test with data: {data}, env: {env}, privateKey: {privateKey}, paychannel_code: "
            f"{paychannel_code}, title: {title}")
        # 调用 perform_order() 方法
        Create().perform_order(env, data, privateKey, pay_channel=paychannel_code)




    # @allure.story("下单接口异常case合计")
    # @pytest.mark.parametrize("data, privateKey, expected_code, expected_msg, title", create_order_data)
    # @pytest.mark.xfail     #断言失败则跳过
    # def test_create_order_error(self,data, privateKey, expected_code, expected_msg, title):
    #         allure.dynamic.title(f"{title}")
    #         response = Create().perform_order(data, privateKey, expected_code=expected_code, expected_msg=expected_msg)
    # #         print(response)
    #
    # @allure.story("限额场景")
    # @pytest.mark.parametrize("data, privateKey, expected_code, expected_msg, title", amount_lmiti)
    # @pytest.mark.xfail     #断言失败则跳过
    # def test_amount_lmiti(self, env, data, privateKey, expected_code, expected_msg, title):
    #         allure.dynamic.title(f"{title}")
    #         response = Create().perform_order(data, privateKey, expected_code=expected_code, expected_msg=expected_msg)
    #         print(response)



if __name__ == '__main__':


    # if os.path.exists("D:/Tiki/results"):
    #     os.system("rm -r D:/Tiki/results")

        pytest.main(["-vs", '--alluredir', 'D:/Tiki/results'])

        # 生成allure报告
        os.system("allure generate D:/Tiki/results -o D:/Tiki/reports --clean")


