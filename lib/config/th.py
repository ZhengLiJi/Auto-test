model = "api_th_env"

th = __import__("lib.config.api_th_env", fromlist=[model])


class Th:
    base_url = th.Base.base_url  # 项目域名 比如 https://www.baidu.com/
    host = th.Base.host
    mysql_port = th.MySQLConfig.port

    # redis_port = dev.Base.redis_port
    # pg_port = dev.PGSQLConfig.port


#

th_config = Th()
print(th_config.base_url)
if __name__ == '__main__':
    pass