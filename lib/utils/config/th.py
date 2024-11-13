model = "api_th_env"

th = __import__("lib.utils.config.api_th_env", fromlist=[model])


class Th:
    base_url = th.Base.base_url
    # host = th.Base.host
    # mysql_port = th.MySQLConfig.port

    # redis_port = dev.Base.redis_port
    # pg_port = dev.PGSQLConfig.port


#

th_config = Th()
print(th_config.base_url)
if __name__ == '__main__':
    pass