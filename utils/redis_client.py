#!/usr/bin/python3

# @Author   : huangtongx
# @Email    : huangtongx@yeah.net
# @Time     : 2019/3/10 17:56
# @Software : PyCharm
# @File     : redis_client.py

from redis import Redis
from config import Config

# 初始化redis实例变量
xtredis = Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    password=Config.REDIS_PASSWORD,
    retry_on_timeout=Config.REDIS_RETRY_ON_TIMEOUT
)


def set(name, value, ex=None):
    """:param key:
    :param value:
    """
    xtredis.set(name=name, value=value, ex=ex)


def get(name):
    """
    Redis根据key获取值
    :param key:
    :return:
    """
    return xtredis.get(name=name)


def delete(name):
    """
    Redis删除数据
    :param key:标识
    """
    xtredis.delete(name)
