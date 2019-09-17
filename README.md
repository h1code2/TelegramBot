# TelegramBot

#### 介绍
使用Python3+Flask做的一个telegram信息推送机器人

#### 使用前请新建config.py配置文件

``` python
class Config(object):
    # Redis数据库配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 'xxx'
    REDIS_PASSWORD = 'xxxxxxxxxxx'
    REDIS_RETRY_ON_TIMEOUT = '2x'

    # telegram机器人token配置
    BOT_TOKEN = '73xxxxx49:AAHDqxxxxxxxxxxxxxxxxxxxxAdQo'
    # 机器人推送接口
    BOT_SEND_MESSAGE_URL = 'https://api.telegram.org/bot{}/sendMessage'.format(BOT_TOKEN)
    # 机器人内部请求连接,自己服务器主机地址
    BOT_REQUEST_URL = 'http://bot.xxx.cn/{}/'
```
config.py配置文件路径说明，config.py文件和app.py同级即可。

#### 字段解释

得到连接后可以GET提交以下字段

| 参数                     | 类型    | 必须  | 说明                                     |
| ------------------------ | ------- | ----- | ---------------------------------------- |
| text                     | String  | True  | 发送的文字内容                           |
| parse_mode               | String  | False | 发送文字内容的样式，可以是Markdown或HTML |
| disable_web_page_preview | Boolean | False | 控制是否展示链接的卡片                   |
| disable_notification     | Boolean | False | 控制是否发送通知                         |