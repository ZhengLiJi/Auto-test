from lib.create_order2 import CreateOrder
from lib.create_payout import Payout
import hashlib
import requests




class Sign:
    

    def order_sign(self):
        keys = sorted(self.data)
        """sorted按照ASCLL从小到大排序"""

        accsiiParams = ""
        orderNo = "TestOrderNo_" + self.time.get_timestamp()  # 测试订单号用时间戳生成
        self.data['orderNo'] = orderNo

        for i in keys:
            if i not in ["sign", "params"]:
                accsiiParams += f"{i}={self.data[i]}"
            elif i == "orderNo":
                accsiiParams += f"{i}={orderNo}"
            elif i == "merchantId":
                accsiiParams += f"{i}={str(self.data[i])}"
            elif i == "productId":
                accsiiParams += f"{i}={str(self.data[i])}"
            elif i == "currency":
                accsiiParams += f"{i}={str(self.data[i])}"

            if i != "sign":
                accsiiParams += '&'

        self.data["params"] = accsiiParams
        accsiiParams += self.privateKey

        return accsiiParams

    def query_sign(self):
        keys = sorted(self.data)
        accsiiParams = ""


        for i in keys:
            if i not in ["sign", "params"]:
                accsiiParams += f"{i}={self.data[i]}"
            elif i == "merchantId":
                accsiiParams += f"{i}={str(self.data[i])}"
            if i != "sign":
                accsiiParams += '&'
        self.data["params"] = accsiiParams
        accsiiParams += self.privateKey

        return accsiiParams


    def get_md5(self, s):
        md = hashlib.md5()
        md.update(s.encode('utf-8'))
        sign = md.hexdigest()
        self.data["sign"] = sign
        return sign
if __name__ == '__main__':
    pass