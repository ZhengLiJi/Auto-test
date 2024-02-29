import random


class Random:
    @staticmethod
    def random_phone(count=11):
        """
        随机生成XX位的手机号码
        :param count: 手机号长度，默认为11位
        :return: phone_number  生成的手机号
        """
        str = ['139', '138', '137', '136', '135', '134', '159', '158', '157', '150', '151', '152', '188', '187', '182',
               '183', '184', '178', '130', '131', '132', '156', '155', '186', '185', '176', '133', '153', '189', '180',
               '181', '177']
        str1 = '0123456789'
        phone_number = random.choice(str) + ''.join(random.choice(str1) for _ in range(count - 3))
        return phone_number

    @staticmethod
    def random_good_name():
        """生成随机商品名"""
        good_name_list = ["牛奶", "咖啡"]
        return random.choice(good_name_list)


if __name__ == '__main__':
    a = Random.random_phone()
    print(a)
