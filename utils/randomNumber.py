#!/usr/bin/python3

# @Author   : huangtongx
# @Email    : huangtongx@yeah.net
# @Time     : 2019/3/10 20:27
# @Software : PyCharm
# @File     : randomNumber.py

import random


def get_random_6_code():
    """随机生成6位数字"""
    str = ""
    for i in range(6):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
    return str
