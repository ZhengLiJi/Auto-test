
import json

class Crade():
    data = {
            'version': 1.0,
            'merchantId': "100119",
            'productId': "2023",
            'currency': 'IDR',
            'orderNo': '',
            'amount': "amount",
            'bankCode': "DANA",
            'accountHolderName': 0,
            'description': 'TestSubject',
            'accountNumber': "081382826301",
            'sign': "{{sign}}",
            "params": "{{}}",
            }

    privateKey = '97fa79f073c7c5e3c97b00b50b156eaa'

    url = 'https://sit.tikipay.co/pay/payout'

    def __init__(self,amount,accountNumber,bankCode):
        data2 = {'amount':amount,'accountNumber':accountNumber,'bankCode':bankCode}

        Crade.data.update(data2)
        print(Crade.data)

if __name__ == '__main__':

    Crade("10000","081382826301","BNI")
    # Xixi(111111,22.33,99)
    pass
