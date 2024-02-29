model = "api_ph_env"

ph = __import__("lib.config.api_ph_env", fromlist=[model])


class Ph:
    base_url = ph.Base.base_url  # 项目域名 比如 https://www.baidu.com/
    host = ph.Base.host
    mysql_port = ph.MySQLConfig.port

    # redis_port = dev.Base.redis_port
    # pg_port = dev.PGSQLConfig.port


#

ph_config = Ph()
print(ph_config.base_url)
if __name__ == '__main__':
    pass