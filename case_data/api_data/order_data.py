import yaml


create_order_data= [

    # 商户id, 产品id, 币种，金额，支付方式，版本信息，， except_code, except_msg

        ({
        'merchantId': '88888',
        'productId': '2023',
        'currency': 'IDR',
        'amount': '10000',
        'payChannel': '17',
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'
    }, "97fa79f073c7c5e3c97b00b50b156eaa", '88015', "merchant not exist", "商户Id错误"),

        ({
        'productId': '2023',
        'currency': 'IDR',
        'amount': '10000',
        'payChannel': '17',
        'version': 1.0,
        'expectPayCodeType': 0,
        'subject': 'TestSubject',
        'payerName': 'test'
    }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "merchantId can not be blank", "商户字段为必填"),

    ({
         'merchantId': '1001191',
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "productId can not be blank", "产品字段为必填参数"),

    ({
         'merchantId': '100119',
         'productId': '20231',
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88032', "productId is not valid", "产品id不存在"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'amount': '10000',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "currency can not be blank", "币种为必填字段"),

    ({
         'merchantId': '100119',
         'productId': '20231',
         'currency': 'ID3',
         'amount': '10000',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "currency can not be blank", "币种不存在"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '999',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88026', "the order amount is too small", "钱包支付金额最少不可以低于1000"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '9999',
         'payChannel': '4',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88026', "the order amount is too small", "VA支付金额最少不可以低于10000"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '9999',
         'payChannel': '12',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88026', "the order amount is too small", "便利店支付金额最少不可以低于10000"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '9999',
         'payChannel': '1',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88026', "the order amount is too small", "信用卡支付金额最少不可以低于10000"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '100000001',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88036', "the order amount is too big", "金额过大"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '1000.11',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "amount should be integer", "金额不支持小数"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '1000a',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88048', "amount should be integer", "金额字段只接受纯数字传参"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "amount can not be blank", "金额字段为必填"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "amount can not be blank", "金额为空"),


    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '10000',
         'payChannel': '',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "payChannel can not be blank", "支付方式不为空"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '1000',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "inner system error, please try again", "支付方式不存在"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '17A.1',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "inner system error, please try again", "请输入有效的paychannel"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '10000000',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "payChannel can not be blank'", "支付方式字段为必填"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '17',
         'version': '',
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "length of version field is too long", "版本信息不为空"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '1000',
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "version can not be blank", "版本信息为必填字段"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '1000',
         'version': '121212',
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "length of version field is too long", "版本信息只支持五位字符串"),


    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test',
         'orderNo': 'TestOrderNo_1710211808034'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88003', "order already exist", "订单已存在"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test',
         'orderNo': 'TestOrderNo_17102118080342132133333333333213213132121321321312312312321'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "length of orderNo field is too long", "订单号超过65个字符串"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test',
         'orderNo': ''
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "length of orderNo field is too long", "订单号不为空"),

    ({
         'merchantId': '100119',
         'productId': '2023',
         'currency': 'IDR',
         'amount': '10000000',
         'payChannel': '17',
         'version': 1.0,
         'expectPayCodeType': 0,
         'subject': 'TestSubject',
         'payerName': 'test'
     }, "97fa79f073c7c5e3c97b00b50b156eaa", '88001', "rderNo can not be blank", "请传入orderNo字段"),
#
]



# 打印 YAML 字符串
with open('create_order_data.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(create_order_data, file, allow_unicode=True)

print(create_order_data)