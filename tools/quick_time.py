# coding:utf-8
import time
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TimeUtils(object):

    @classmethod
    def zero_timestamp(cls, timestamp=None):
        """
        获取当天0点时间戳
        date_str: 日期字符串，如果没有默认使用当前时间
        """
        if not timestamp: timestamp = int(time.time())
        return cls.date2timestamp(cls.timestamp2date(timestamp))
        # return timestamp - timestamp % 86400 + time.timezone

    @classmethod
    def date2timestamp(cls, date_str, fmt="%Y-%m-%d"):
        """
        按照fmt的格式，将一个日期转换成时间戳
        date_str: 日期字符串 2017-06-30
        fmt: 日期的格式 %Y-%m-%d
        """

        return int(time.mktime(time.strptime(date_str, fmt)))

    @classmethod
    def timestamp2date(cls, timestamp, fmt="%Y-%m-%d"):
        """
        按照fmt的格式，将一个时间戳转换成日期
        timestamp: 时间戳
        fmt: 期望得到的格式. eg: %Y-%m-%d %H:%M:%S
        """

        return time.strftime(fmt, time.localtime(timestamp))

    @classmethod
    def passNday(cls, n=0, fmt="%Y-%m-%d"):
        """
        获取过去N天的日期
        n: n天数

        return: 2017-06-30
        """

        return (datetime.datetime.today() - datetime.timedelta(n)).strftime(fmt)

    @classmethod
    def futureNday(cls, n=0, fmt="%Y-%m-%d"):
        """
        获取未来N天的日期
        n: n天数

        return: 2017-06-30
        """

        return (datetime.datetime.today() + datetime.timedelta(n)).strftime(fmt)

    @staticmethod
    def now_timestamp_13():
        millis = int(round(time.time() * 1000))
        return millis


if __name__ == '__main__':
    t=time.time()
    print TimeUtils.timestamp2date(t, '%Y-%m-%d %H:00:00')
    print t

    #  %Y%m%d%H%M%S
    # print TimeUtils.passNday(2)
    # print TimeUtils.futureNday(2)
    # print TimeUtils.date2timestamp(TimeUtils().futureNday(2))
    # print TimeUtils.passNday(0)
    # print TimeUtils.passNday(4)
    # print TimeUtils.futureNday(4)
    # print TimeUtils.zero_timestamp()
