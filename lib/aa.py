import time
import hashlib
import requests
from lib.ll import Crade



def mill_ms():
    return str(int(time.time() * 1000))

class Xis(Crade):
    def __init__(self):
        pass




    def Five(self):
        Crade(10000,)
        # super(Xis, self).__init__()


        keys = sorted(Crade.data)
        accsiiParams = ""
        orderNo = "TestOrderNo_" + mill_ms()
        Crade.data['orderNo'] = orderNo
        print(orderNo)

        for i in list(keys):
            if i == "orderNo":
                accsiiParams = accsiiParams + i + "=" + Crade.data[i]
            elif i == "merchantId":
                accsiiParams = accsiiParams+ i + "=" + Crade.data[i]
            elif i == "productId":
                accsiiParams = accsiiParams+ i + "=" + Crade.data[i]
            elif i == "currency":
                accsiiParams = accsiiParams+ i + "=" + Crade.data[i]
            elif i != "sign" and i != "params":
                accsiiParams = accsiiParams+ i + "=" + str(Crade.data[i])


            if i != "sign" and i != "params":
                accsiiParams = accsiiParams + "&"
            elif i != "sign":
                accsiiParams = accsiiParams
                Crade.data['orderNo'] = orderNo

        Crade.data['params'] = accsiiParams

        accsiiParams = accsiiParams[0:len(accsiiParams)-1] + Crade.privateKey

        return accsiiParams


    def get_md6(self,ss):
        md = hashlib.md5()
        md.update(ss.encode('utf-8'))
        sign = md.hexdigest()
        Crade.data["sign"] = sign
        return sign


    def post_create_orderr(self):
        return Crade.url + '?' + Crade.data["params"] + 'sign=' + Crade.data['sign']




if __name__ == '__main__':
    # super(Xis).__init__("10000","081382826301","BNI")
    accsiiParams = Xis().Five()
    sign = Xis().get_md6(accsiiParams)
    create_order_url = Xis().post_create_orderr()
    print(Crade.data["params"])
    print(Crade.data['sign'])
    print(create_order_url)
    resp = requests.post(create_order_url)
    print(resp.json())



