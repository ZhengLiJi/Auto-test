import yaml
from case_data.api_data.pay_channel import *



create_order_data= [

    # 商户id, 产品id, 币种，金额，支付方式，版本信息，， except_code, except_msg

    ({
        'merchantId': 1001,
        'productId': productId_119,
        'currency': 'IDR',
        'amount': '10000',
        'payChannel': dana,
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'
    }, key_119, '88012', "merchant not exist", "商户Id错误"),

    ({
        'productId': productId_119,
        'currency': 'IDR',
        'amount': '10000',
        'payChannel': dana,
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'
    }, key_119, '88001', "merchantId can not be blank", "商户字段为必填"),

    ({
         'merchantId': "" ,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "merchant not exist", "商户id不为空"),

    ({
         'merchantId': '100119',
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "productId can not be blank", "产品字段为必填参数"),

    ({
         'merchantId': merchantId_119,
         'productId': '20231',
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88032', "productId is not valid", "产品id不存在"),

    ({
         'merchantId': merchantId_119,
         'productId': '',
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "productId can not be blank", "产品id不为空"),


    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'amount': '10000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "currency can not be blank", "币种为必填字段"),

    ({
         'merchantId': merchantId_119,
         'productId': '20231',
         'currency': 'ID3',
         'amount': '10000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "currency can not be blank", "请输入有效的币种"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '1000.11',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "amount should be integer", "金额不支持小数"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '1000a',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88048', "amount should be integer", "金额字段只接受纯数字传参"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "amount can not be blank", "金额字段为必填"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "amount can not be blank", "金额为空"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': '',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "payChannel can not be blank", "支付方式不为空"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '1000',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "inner system error, please try again", "支付方式不存在"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '17A.1',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "inner system error, please try again", "请输入有效的paychannel"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000000',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "payChannel can not be blank'", "支付方式字段为必填"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': dana,
         'version': '',
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "length of version field is too long", "版本信息不为空"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '1000',
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "version can not be blank", "版本信息为必填字段"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '1000',
         'version': '121212',
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "length of version field is too long", "版本信息只支持五位字符串"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test',
         'orderNo': 'TestOrderNo_1710211808034'
     }, key_119, '88003', "order already exist", "订单已存在"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test',
         'orderNo': 'TestOrderNo_17102118080342132133333333333213213132121321321312312312321'
     }, key_119, '88001', "length of orderNo field is too long", "订单号超过65个字符串"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test',
         'orderNo': ''
     }, key_119, '88001', "length of orderNo field is too long", "订单号不为空"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88001', "rderNo can not be blank", "请传入orderNo字段"),
#
] #收款异常case
user_routing =[
    ({
        'merchantId': merchantId_119,
        'productId': productId_119,
        'currency': 'IDR',
        'amount': '10000',
        'payerPhone': '0888888881',
        'payChannel': dana,
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'},
    key_119, xendit, "xendit"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payerPhone': '0888888882',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, xendit2, "xendit2"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payerPhone': '0888888883',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, xendit3, "xendit3"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payerPhone': '0888888885',
         'payChannel': permata,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, faspay, "faspay"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payerPhone': '0888888886',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, oy, "oy"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payerPhone': '0888888888',
         'payChannel': '15',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, gv, "gv"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payerPhone': '0888888889',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, xendit5, "xendit5"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '15000',
         'payerPhone': '081806708607',
         'payChannel': '4',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, mcpay,"mcpay"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payerPhone': '0888888892',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, mpi,"MPI"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payerPhone': '0888888892',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, dana_channel,"DANA"),

]    #收款用户标识
amount_routing = [
    ({
         'merchantId': merchantId_149,
         'productId': productId_149,
         'currency': 'IDR',
         'amount': '5000',
         'payChannel': linkaja,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_149, oy, "单个支付方式的金额区间-路由为oy"),

    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '6000',
         'payChannel': ovo,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_888, xendit, "多个支付方式的金额区间-路由为xendit"),


    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '20008',
         'payChannel': shopeepay,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, xendit2, "单个商户的金额区间-xendit2"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10005',
         'payChannel': '19',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, faspay, "多个商户的金额区间-faspay"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '5000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, mpi, "单个商商户和单个支付方式的金额区间-MPI"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '40000',
         'payChannel': '4',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, oy, "单个商商户和多个支付方式的金额区间-oy"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '20000',
         'payChannel': '8',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, xendit, "多个商商户和单个支付方式的金额区间-xendit"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '20005',
         'payChannel': '15',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, xendit, "多商户和多支付方式的金额区间场景-xendit"),

]  #收款金额路由
normal_routing = [
    ({
        'merchantId': merchantId_149,
        'productId': productId_149,
        'currency': 'IDR',
        'amount': '100000',
        'payChannel': bri,
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'},
    key_149, xendit, "单个类型的普通路由"),

    ({
        'merchantId': merchantId_149,
        'productId': productId_149,
        'currency': 'IDR',
        'amount': '100000',
        'payChannel': linkaja,
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'},
    key_149, xendit, "单个支付方式的普通路由"),

    ({
         'merchantId': merchantId_149,
         'productId': productId_149,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': cimb,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_149, oy, "多个支付方式的普通路由"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '100000',
         'payChannel': bri,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_119, oy, "单个商户及单个类型的普通路由"),

    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '100000',
         'payChannel': shopeepay,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_888, xendit, "多个商户及单个类型的普通路由"),

    ({
        'merchantId': merchantId_119,
        'productId': productId_119,
        'currency': 'IDR',
        'amount': '100000',
        'payChannel': dana,
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'},
    key_119, mpi, "单个商户及单个支付方式的普通路由"),

    ({
         'merchantId': merchantId_149,
         'productId': productId_149,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_149, dana_channel, "单个商户及多个支付方式的普通路由"),

    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '100000',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_888, oy, "多个商户及单个支付方式的普通路由"),

    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '100000',
         'payChannel': linkaja,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_888, oy, "多个商户及多个支付方式的普通路由"),

] #收款普通路由
amount_lmiti = [
    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '9999',
         'payChannel': '19',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_888, '88026', "the order amount is too small",
     "指定商户钱包类型最小限额为10000"),

    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '100001',
         'payChannel': '19',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_888, '88036', "the order amount is too big",
     "指定商户钱包类型最大限额为100000"),

    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '99999',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_888, '88026', "the order amount is too small",
     "指定商户的支付方式DANA类型最小限额为100000"),

    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '1000001',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_888, '88036', "the order amount is too big",
     "指定商户的支付方式DANA最大限额为1000000"),


    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '999',
         'payChannel': '18',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88026', "the order amount is too small",
     "默认商户的钱包类型最小限额为1000"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '100000001',
         'payChannel': '18',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88036', "the order amount is too big",
     "默认商户的钱包类型最大限额为100000000"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '9998',
         'payChannel': '38',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88026', "the order amount is too small",
     "默认商户的支付方式最小限额为9999"),


    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '100000',
         'payChannel': '38',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '88036', "the order amount is too big",
     "默认商户的支付方式最大限额为99999"),

] #收款限额场景
rate_case = [
    ({
         'merchantId': merchantId_149,
         'productId': productId_149,
         'currency': 'IDR',
         'amount': '1000',
         'payerPhone': '0888888881',
         'payChannel': linkaja,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_149, 0, 0, "没有配置费率"),
    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '1000',
         'payerPhone': '0888888881',
         'payChannel': dana,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_888, 20, 15, "商户比例收费及渠道比例收费"),
    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '10000',
         'payerPhone': '0888888881',
         'payChannel': bni,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_888, 1111, 1500, "商户基础费率及渠道基础费率"),
    ({
         'merchantId': merchantId_888,
         'productId': productId_888,
         'currency': 'IDR',
         'amount': '10000',
         'payerPhone': '0888888881',
         'payChannel': shopeepay,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'},
     key_888, 800, 1150, "商户比例收费+基础费率 及 渠道比例收费+基础费率"),


] #收款费率场景
features_case = [
    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': 16,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '200', "0", "qris返回支付码"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': 16,
         'version': 1.0,
         'expectPayCodeType': 1,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '200', "1", "qris返回支付链接"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': 12,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '200', "0", "便利店返回支付码"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': 12,
         'version': 1.0,
         'expectPayCodeType': 1,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '200', "1", "便利店返回支付链接"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': 4,
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '200', "0", "VA返回支付码"),

    ({
         'merchantId': merchantId_119,
         'productId': productId_119,
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': 4,
         'version': 1.0,
         'expectPayCodeType': 1,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, key_119, '200', "1", "VA返回支付链接"),
] #其他字段的特殊场景
