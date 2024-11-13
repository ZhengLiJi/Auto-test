#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/20 16:40
# @Author  : zheng
# @File    : pay_channel.py
# @Software: PyCharm

#各支付方式编码
ovo = '15'
qris = '16'
dana = '17'
linkaja = '18'
shopeepay = '19'
astaypay = '38'
permata = '3'
bni = '4'
bca = '5'
cimb = '6'
mandiri = '8'
bri = '9'

TrueMoney = '24'
LINE_PAY = '27'
ShopeePay_th = '28'
PromptPay = '29'
SCB = '40'
KBank = '41'
BBL = '42'
KTB = '43'
BAY = '44'

GrabPay = '31'
Maya = '32'
GCash = '33'
ShopeePay_ph = '36'
BPI = '34'
UBP = '35'
Eleven = '30'
Cebuana = '37'

TNG = '50'
Boost = '51'
MCash = '52'
GrabPay_my = '53'
ShopeePay_my = '57'
FPX = '55'

MOMO = '76'
ZALOPAY = '75'
ShopeePay_vn = '72'
VNPTPAY = '73'
WOORI = '65'

BOLETO = '60'
PIX = '61'
BANK_TRANSFER = '81'
AME = '77'
PicPay = '78'
PayPal = '79'
MERCADO_PAGO = '80'

PayCash = '82'
OXXO = '83'
MX_BANK_TRANSFER = '84'

ETH = 'ETH'
BSC = 'BSC'
TRON = 'TRON'
POLYGON = 'POLYGON'

#各渠道编码

doku = 1
midtrans = 2
mcpay = 3
nicepay = 4
tikipay = 5
mobbpay = 6
xendit = 7
alto = 9
xendit2 = 10
oy = 11
mpi = 12
xendit3 = 13
faspay = 14
gv = 15
xendit4 = 16
gv2 = 17
gv3 = 18
zipay = 19
zipay2 = 20
duitku = 21
xendit5 = 22
oy2 = 23
dana_channel = 24
paydibs = 41
flashpay = 30
lianlianpay = 31
flashpay2 = 32
xendit_ph = 33
xendit2_ph = 34
toctop = 42
alterra = 43
lianlian_global = 44
veloce = 45
xendit_my = 46
xendit_vn = 47
xendit_th = 48
huawei_mm = 49
bluezi = 50
redisionpay = 51
liquido = 52
liquido_mx = 53

#断言paycode支付链接
dana_link = ['https://m.dana.id', "https://link.dana.id"]
test_link = 'https://checkouttest.lipperpay.com/mock'
shopeepay_link = "https://pay.airpay.co.id/h5pay"

#各个商户
merchantId_149 = '100149'
productId_149 = '2071'
key_149 = '8kc8u438cg877uh387fu65ll012tv6bu'

merchantId_119 = '100119'
productId_119 = '2023'
key_119 = '97fa79f073c7c5e3c97b00b50b156eaa'

merchantId_888 = '88888'
productId_888 = '1099'
key_888 = 'akiki29dk39dlove0329djustin'


ph_merchantId = '100170'
ph_productId = '2081'
ph_key = '300a1baf3fe8de94b406ff64ef56c5e9'

th_merchantId = '100165'
th_productId = '2080'
th_key = 'fcc3b42f6f0cd97aa53cedd124c2e91f'

vn_merchantId = '8890273245'
vn_productId = '2161'
vn_key = '5d6c24030aab7b4ccf6b9fec6cbfdd8a'

my_merchantId = '8890273246'
my_productId = '2162'
my_key = '1651c95bb281d45a07e34a003dfc7c83'

us_merchantId = '8890273242'         #巴西美金
us_productId = '2158'
us_key = '9715c13d29c2df6599ae04a5a22ff037'

br_merchantId = '8890273340'         #巴西本地
br_productId = '2248'
br_key = 'f2341e65d5e85c644b59c69266367b37'

mx_merchantId = '8890273249'
mx_productId = '2165'
mx_key = '8b10641fd40be6d3a959eedabb7b022a'

web3_merchantId = '8890273320'
web3_productId = '2228'
web3_key = '814322b2ab83b40737112522e62aa8d4'


#各个国家币种
currency_IDR = 'IDR'
currency_PHP = 'PHP'
currency_THB = 'THB'
currency_VND = 'VND'
currency_MYR = 'MYR'
currency_BRL = 'BRL'
currency_MXN = 'MXN'
currency_USDT = 'USDT'

sit = 'sit'
la = 'api-la'
ph = 'api-ph'
idr = 'api'
th = 'api-th'
pg = 'pg'


