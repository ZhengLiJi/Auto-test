from lib.utils.database.mysql.mysql import MySQL
import pymysql

def mysql_wrap(cls):
    def inner():
        return MySQL(cls)

    return inner


@mysql_wrap
class Dbtrade:
    database = "trade"

class Dbusercenter:
    database = "usercenter"


class Store:
    pass


if __name__ == '__main__':
    a = Dbtrade()
    rsp = a.search("select * from order_bill where id = 1")
    print(rsp)
    pass
