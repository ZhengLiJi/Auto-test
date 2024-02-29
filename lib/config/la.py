model = "api_la_env"

la = __import__("lib.config.api_la_env", fromlist=[model])


class La:
    base_url = la.Base.base_url  # 项目域名 比如 https://www.baidu.com/
    host = la.Base.host
    mysql_port = la.MySQLConfig.port

    # redis_port = dev.Base.redis_port
    # pg_port = dev.PGSQLConfig.port


#

la_config = La()
print(la_config.base_url)
if __name__ == '__main__':
    pass