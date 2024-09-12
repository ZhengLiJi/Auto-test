model = "sit_env"

sit = __import__("lib.utils.config.sit_env", fromlist=[model])


class Sit:
    base_url = sit.Base.base_url  # 项目域名 比如 https://www.baidu.com/

    mysql_host = sit.MySQLConfig.host
    mysql_port = sit.MySQLConfig.port
    mysql_user = sit.MySQLConfig.user
    mysql_password = sit.MySQLConfig.password
    #
    # redis_port = dev.Base.redis_port
    # pg_port = dev.PGSQLConfig.port


#

sit_config = Sit()

if __name__ == '__main__':
    pass
#     # a = Dev
    # # print(a.redis_port)
    # print(a)
    # print(a.base_url)


