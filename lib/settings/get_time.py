from datetime import datetime, timedelta
import pytz
import time
from lib.settings.logger import log
import calendar


class GetTime:
    """
    格式化日期 time.strftime(format[, t])
    """

    @staticmethod
    def get_current_est_date(fmt="%Y-%m-%d"):
        """
        当前美东日期
        Args:
            fmt:
        Returns:
        """
        now = datetime.now(tz=pytz.timezone('EST'))
        return now.date().strftime(fmt)

    @staticmethod
    def get_current_est_time(fmt="%Y-%m-%d %H:%M:%S"):
        """
        当前美东时间
        Args:
            fmt:
        Returns:
        """
        now = datetime.now(tz=pytz.timezone('EST'))
        return now.strftime(fmt)

    @staticmethod
    def current_data():
        current_date = time.strftime('%Y-%m-%d')
        return current_date

    @staticmethod
    def current_time():
        current_time = time.strftime('%H_%M_%S')
        return current_time

    @staticmethod
    def date_time():
        data_time = time.strftime('%Y-%m-%d %H:%M')
        return data_time

    @staticmethod
    def date_time_s():
        data_time = time.strftime('%Y-%m-%d %H:%M:%S')
        return data_time

    @staticmethod
    def get_timestamp():
        """
        返回毫秒级时间戳
        :return:
        """
        time_stamp = int(round(time.time() * 1000))
        return str(time_stamp)


    @staticmethod
    def get_timestamp_s():
        """
        返回秒级时间戳
        :return:
        """
        time_stamp = int(round(time.time()))
        return time_stamp

    @staticmethod
    def get_timestamp_delta_s(hour=0, day=0, minute=0, second=0, week=0):
        """
        获取时间戳
        :return:
        """
        now = datetime.now()
        delta = timedelta(days=day, hours=hour, minutes=minute, seconds=second, weeks=week)
        date = (now + delta).timestamp()
        return int(date)

    @staticmethod
    def get_date_time(expire_time, ftr="%Y-%m-%d"):
        """
        根据时间戳获取日期 %Y-%m-%d
        Args:
            expire_time ():
            ftr: 格式

        Returns:
        """
        time_local = time.localtime(int(expire_time))
        dt = time.strftime(ftr, time_local)
        return dt
    # staticmethod静态方法只是名义是的归属类管理，不能使用类变量和实例变量，是类的工具包
    @staticmethod
    def get_s_timestamp():
        """
        返回秒级时间戳
        """
        time_stamp = int(round(time.time()))
        return str(time_stamp)

    @staticmethod
    def now_milliseconds():
        """
        返回毫秒时间戳
        """

        return str(int(time.time() * 1000))







    @staticmethod
    def date_to_timestamp(date_time, ftr='%Y-%m-%d %H:%M:%S'):
        """
        日期转成时间戳
        """
        time_stamp = int(time.mktime(time.strptime(date_time, ftr)))
        return str(time_stamp)

    @staticmethod
    def timestamp_to_date(timestamp, ftr='%Y-%m-%d %H:%M:%S'):
        """
        日期转成时间戳
        """
        date = time.strftime(ftr, time.localtime(int(timestamp)))
        return date

    @staticmethod
    def time_method(hour=0, day=0, minute=0, second=0, week=0, ftr='%Y-%m-%d'):
        now_t = datetime.now()
        lead_time = timedelta(days=day, hours=hour, minutes=minute, seconds=second, weeks=week)
        f_time = now_t + lead_time
        all_time = f_time.strftime(ftr)
        return all_time

    @staticmethod
    def get_utc_time():
        return datetime.utcnow()

    @staticmethod
    def get_utc_timestamp():
        # return int(time.mktime(datetime.utcnow().utctimetuple()))
        current_datetime = datetime.utcnow()
        current_timetuple = current_datetime.utctimetuple()
        current_timestamp = calendar.timegm(current_timetuple)
        return current_timestamp

    @staticmethod
    def get_option_time(week_day=5, offset=0):
        """
        获取本周 或者下周的 周x
        当日是 周一到周五 返回本周五
        当日是周六 周日 返回下周 五
        :param week_day:
        :return:
        """
        expected = int(week_day) - 1
        d = datetime.now()
        today = d.weekday()
        this_week = (0, 1, 2, 3, 4)
        next_week = (5, 6)
        t = None
        if today in this_week:
            t = GetTime.time_method(day=expected - today + offset, ftr="%Y%m%d")
            log.info(f"期权到期日是{t}")

        if today in next_week:
            t = GetTime.time_method(day=expected + 7 - today + offset, ftr="%Y%m%d")
            log.info(f"期权到期日是{t}")

        assert t, "获取时间错误"
        return t

    @staticmethod
    def date_gap(start_date: str, end_date: str):
        """
        计算两个日期相差多少天
        Args:
            start_date: 20211228
            end_date: 20211231
        Returns:
        """
        old = datetime(int(start_date[0:4]), int(start_date[4:6]), int(start_date[6:8]))
        now = datetime(int(end_date[0:4]), int(end_date[4:6]), int(end_date[6:8]))
        count = (now - old).days
        return count

    @staticmethod
    def get_tz_utc_time(day=0, hour=0, minute=0, second=0, week=0, microseconds=0, milliseconds=0, spec='milliseconds'):
        """
        获取 tz 格式的 utc 时间
            2022-05-14T12:13:57.859Z
        """
        delta = timedelta(days=day, seconds=second, microseconds=microseconds, minutes=minute, hours=hour,
                          weeks=week, milliseconds=milliseconds)
        expire = datetime.utcnow() + delta
        utc_time = expire.isoformat(timespec=spec) + 'Z'
        return utc_time

if __name__ == '__main__':
    pass

