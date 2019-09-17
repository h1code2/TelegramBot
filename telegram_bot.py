#!/usr/bin/python3

# @Author   : huangtongx
# @Email    : huangtongx@yeah.net
# @Time     : 2019/3/10 19:49
# @Software : PyCharm
# @File     : telegram_bot.py

import requests
import telebot
# from telebot import types

from config import Config

bot = telebot.TeleBot(Config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, '你好，我是消息推送助手，你可以使用/add命令，添加一个推送消息连接。')


@bot.message_handler(commands=['help'])
def help(msg):
    text = '[消息助手Bot使用帮助](https://telegra.ph/Telegram消息助手使用-03-11)'
    bot.send_message(msg.chat.id, text, parse_mode='Markdown')


@bot.message_handler(commands=['add'])
def add(msg):
    chat_id = msg.chat.id
    conn = requests.post(
        url=Config.BOT_REQUEST_URL.format('add'),
        data={
            'chat_id': chat_id
        }
    )
    result = conn.json()
    bot.send_message(msg.chat.id, result.get('message') + result.get('data').get('url'))


@bot.message_handler(commands=['remove'])
def remove(msg):
    chat_id = msg.chat.id
    conn = requests.post(
        url=Config.BOT_REQUEST_URL.format('remove'),
        data={
            'chat_id': chat_id
        }
    )
    result = conn.json()
    bot.send_message(msg.chat.id, result.get('message'))


@bot.message_handler()
def other(msg):
    return bot.send_message(msg.char.id, '我的世界很美好的')


if __name__ == '__main__':
    bot.polling()
