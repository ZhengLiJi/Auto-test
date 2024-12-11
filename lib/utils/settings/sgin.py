import hashlib
merchantId = '100119'  # 替换为您的商户ID
productId = '2023'  # 替换为您的产品ID
currency = 'IDR'  # 货币类型
amount = 20000  # 金额
payChannel = 15  # 支付渠道
subject = 'PTWaltDisneyIndonesia'
goodsDetail = 'test'
payerName = 'test'
payerPhone = '08123456789714'
privateKey = '97fa79f073c7c5e3c97b00b50b156eaa'  # 替换为您的签名密钥

class Sign:

    @staticmethod
    def generate_params(data):
        sorted_params = sorted(data.items(), key=lambda x: x[0])
        accsii_params = "&".join([f"{k}={v}" for k, v in sorted_params if k != "sign"])
        return accsii_params

    @staticmethod
    def get_md5(s):
        md = hashlib.md5()
        md.update(s.encode('utf-8'))
        return md.hexdigest()

    @staticmethod
    def sign1(data, private_key):
        params = Sign.generate_params(data) + private_key
        return Sign.get_md5(params)


# 示例用法
if __name__ == '__main__':
    # data = {
    #     'version': 1.0,
    #     'merchantId': 100119,
    #     'productId': 2023,
    #     'currency': 'IDR',
    #     'amount': 110,
    #     'bankCode': 'DANA',
    #     'description': 'test',
    #     'accountHolderName': 'user_dana',
    #     'accountNumber': '081328076003',
    #     "email": "guanxinran@tikipay.co",
    #     'orderNo': 'TestOrderNo_1709804705258'
    # }
    data = {
        'version': '1.0',
        'merchantId': merchantId,
        'productId': productId,
        'currency': currency,
        'orderNo': 'ORD286877',
        'amount': amount,
        'payChannel': payChannel,
        'subject': subject,
        'goodsDetail': goodsDetail,
        'payerName': payerName,
        'payerPhone': payerPhone
    }


    # data = {'"amount"=2785.25&"callbackUrl"=https://middlepay.abilitylkcat.com/api_server/v2/finance/abroad/quartet/callback/order/IJ227522338901825882075835454676/dlabroad&currency=PHP&expectPayCodeType=1&goodsDetail=Extra coins 2499 + Extra VIP 30 days&merchantId=89058&orderNo=IJ227522338901825882075835454676&payChannel=33&payerEmail=fausto.schaden@elc.com&payerName=Fletcher Hayes&payerPhone=63965205743&productId=3057&returnUrl=https://h5.maverickmeki.com/middle-bill/xamrep/&sign=67d26c018a3e511ca07bbd2c950c0d68&subject=Coins 49990&version=1.0'}


    #
    private_key = '97fa79f073c7c5e3c97b00b50b156eaa'

    params = Sign.generate_params(data)
    md5_hash = Sign.get_md5(params + private_key)
    print("Params:", params)
    print("MD5 Hash:", md5_hash)

    pass