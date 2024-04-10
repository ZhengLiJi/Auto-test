import hashlib

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
    #
    # private_key = '97fa79f073c7c5e3c97b00b50b156eaa'
    #
    # params = Sign.generate_params(data)
    # md5_hash = Sign.get_md5(params + private_key)
    # print("Params:", params)
    # print("MD5 Hash:", md5_hash)

    pass