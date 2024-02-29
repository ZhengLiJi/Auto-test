model = "sit_env"

sit = __import__("lib.config.sit_env", fromlist=[model])


class Sit:
    base_url = sit.Base.base_url  # 项目域名 比如 https://www.baidu.com/
    host = sit.Base.host
    mysql_port = sit.MySQLConfig.port

    # redis_port = dev.Base.redis_port
    # pg_port = dev.PGSQLConfig.port


#

sit_config = Sit()
print(sit_config.base_url)
if __name__ == '__main__':
    pass
#     # a = Dev
    # # print(a.redis_port)
    # print(a)
    # print(a.base_url)


