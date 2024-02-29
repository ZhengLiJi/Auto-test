model = "api_pg_env"

pg = __import__("lib.config.api_pg_env", fromlist=[model])


class Pg:
    base_url = pg.Base.base_url  # 项目域名 比如 https://www.baidu.com/
    host = pg.Base.host
    mysql_port = pg.MySQLConfig.port

    # redis_port = dev.Base.redis_port
    # pg_port = dev.PGSQLConfig.port


#

pg_config = Pg()
print(pg_config.base_url)
if __name__ == '__main__':
    pass