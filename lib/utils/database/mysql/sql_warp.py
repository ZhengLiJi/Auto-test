from lib.utils.database.mysql.mysql import MySQL
import pymysql

def mysql_wrap(cls):
    def inner():
        return MySQL(cls)

    return inner


@mysql_wrap
class Dbtrade:
    database = "trade"


@mysql_wrap
class Dbusercenter:
    database = "usercenter"


class Store:
    pass


if __name__ == '__main__':

    a = Dbtrade()
    # b = Dbusercenter()
    rsp = a.search("select * from order_bill order by id desc limit 1")
    # s = rsp[0]["create_time"].year
    # c = rsp[0]["create_time"].month
    print(rsp)



