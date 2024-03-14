# -*- coding: utf-8 -*-
import time

from   lib.base_utils import BaseUtils as bb


idr_data = (100119, 2023, "IDR", 10000, "97fa79f073c7c5e3c97b00b50b156eaa", 1.0, )
thb_data = (100165, 2080, "THB", 30, 'fcc3b42f6f0cd97aa53cedd124c2e91f')
php_data = (100170, 2081, "PHP", 50, "300a1baf3fe8de94b406ff64ef56c5e9")
vnd_data = (8890273245, 2161, "VND", 10000, '5d6c24030aab7b4ccf6b9fec6cbfdd8a')
myr_data = (8890273246, 2162, "MRY", 1, '1651c95bb281d45a07e34a003dfc7c83')
brl_data = (8890273242, 2158, "BRL", 10, "9715c13d29c2df6599ae04a5a22ff037")
mxn_data = (8890273249, 2165, "MXN", 1, '8b10641fd40be6d3a959eedabb7b022a')

pay_channels = {
    'xendit': (1, 3, 4, 5, 6, 8, 9, 12, 15, 16, 17, 18, 19, 38),
    'oy': (3, 4, 5, 6, 8, 9, 12, 15, 16, 17, 18, 19),
    "faspay": (3, 4, 6, 8, 9, 12, 16, 17, 18, 19),
    'gv': (3, 4, 6, 12, 16),
    'dana': (16, 17),
    'mpi': (1, 3, 4, 5, 6, 8, 9, 12, 15, 16, 17, 18, 19, 38),

    'xendit_th': (24, 27, 28, 29, 40, 41, 42, 43, 44),
    'flashpay': (29, 40, 41),
    'lianlianpay': (24, 27, 28, 29, 40, 41),
    'flashpay2': (29, 40, 41),

    'xendit_ph': (30, 31, 32, 33, 34, 35, 36, 37),
    'xendit_ph2': (30, 31, 32, 33, 34, 35, 36, 37),

    'paydibs': (51, 52, 53, 55),
    '2c2p': (),

    'luquido': (60, 61, 77, 78, 79, 80, 81),
    'luquido_mx': (81, 82, 83)

}

code_data = [200, 88005, 88011, 88002, 88003, 88004, 88010, 88012, 88014, 88015, 88021, 88022, 88023, 88024, 88025, 88026, 88032]




"""监控各渠道的支付下单data"""
# print(xendit)
def generate_data(channel, payer_phone, data,privateKey, code,msg,):
    return {
        'merchantId': str(data[0]),
        'productId': str(data[1]),
        'currency': data[2],
        'amount': str(data[3]),
        'payerPhone': payer_phone,
        'payChannel': str(channel),
               'version': 1.0,
               'expectPayCodeType': 0,
               'subject': 'TestSubject',
               'payerName': 'test',
           }, privateKey, code, msg
    # xendit1_data = [generate_data(channel, pay_channels['xendit']['phone'], idr_data) for channel in pay_channels['xendit']['channels']]
    #
xendit1_data =[({'merchantId': '100119', 'productId': '2023', 'currency': 'IDR', 'amount': '10000', 'payerPhone': '0888888881', 'payChannel': '1', 'version': 1.0, 'expectPayCodeType': 0, 'subject': 'TestSubject', 'payerName': 'test'}, '97fa79f073c7c5e3c97b00b50b156eaa', '200', 'SUCCESS'), ({'merchantId': '100119', 'productId': '2023', 'currency': 'IDR', 'amount': '10000', 'payerPhone': '0888888881', 'payChannel': '3', 'version': 1.0, 'expectPayCodeType': 0, 'subject': 'TestSubject', 'payerName': 'test'}, '97fa79f073c7c5e3c97b00b50b156eaa', '200', 'SUCCESS')]
print(xendit1_data)
# xendit2_data = [generate_data(channel, "0888888882", idr_data) for channel in xendit]
# # xendit3_data = [generate_data(channel, "0888888883", idr_data) for channel in xendit]
# # xendit5_data = [generate_data(channel, "0888888889", idr_data) for channel in xendit]
# faspay_data = [generate_data(channel, "0888888885", idr_data) for channel in pay_channels['faspay']]
# oy_data = [generate_data(channel, "0888888886", idr_data,200) for channel in pay_channels["oy"]]
# gv_data = [generate_data(channel, "0888888888", idr_data) for channel in pay_channels["gv"]]
# dana_data = [generate_data(channel, "0888888893", idr_data) for channel in pay_channels["dana"]]
# mpi_data = [generate_data(channel, "0888888892", idr_data) for channel in pay_channels["mpi"]]
#
# xendit_th_data =  [generate_data(channel, "08888888881", thb_data) for channel in pay_channels["xendit_th"]]
# lianlianpay_data = [generate_data(channel, "08888888882", thb_data) for channel in pay_channels["lianlianpay"]]
# flashpay_data = [generate_data(channel, "08888888883", thb_data) for channel in pay_channels["flashpay"]]
# flashpay2_data = [generate_data(channel, "08888888884", thb_data) for channel in pay_channels["flashpay2"]]
#
# xendit_ph_data = [generate_data(channel, "0888888888335", php_data) for channel in pay_channels["xendit_ph"]]
# # xendit2_ph_data = [generate_data(channel, "0888888888154", php_data) for channel in pay_channels["xendit_ph2"]]
#
# paydibs_data = [generate_data(channel, "08888888883213", myr_data) for channel in pay_channels["paydibs"]]
#
# luquido_data = [generate_data(channel, "08888888883213", brl_data) for channel in pay_channels["luquido"]]
#
# luquido_mx_data = [generate_data(channel, "088888888823123", mxn_data) for channel in pay_channels["luquido_mx"]]
"""监控各渠道的支付下单data"""
# # 存储生成的数据列表
# generated_data = {}
