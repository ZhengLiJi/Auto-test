model = "api_env"

id = __import__("lib.config.api_env", fromlist=[model])


class Id:
    base_url = id.Base.base_url  # 项目域名 比如 https://www.baidu.com/
    host = id.Base.host
    mysql_port = id.MySQLConfig.port

    # redis_port = dev.Base.redis_port
    # pg_port = dev.PGSQLConfig.port


#

id_config = Id()
print(id_config.base_url)
if __name__ == '__main__':
    pass