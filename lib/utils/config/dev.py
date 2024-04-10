model = "dev_env"

dev = __import__("lib.config.dev_env", fromlist=[model])


class Dev:
    base_url = dev.Base.base_url  # 项目域名 比如 https://www.baidu.com/
    host = dev.Base.host
    mysql_port = dev.MySQLConfig.port
    # redis_port = dev.Base.redis_port
    # pg_port = dev.PGSQLConfig.port




dev_config = Dev()
print(dev_config.base_url)
if __name__ == '__main__':
    pass
    # a = Dev
    # # print(a.redis_port)
    # print(a)
    # print(a.base_url)
