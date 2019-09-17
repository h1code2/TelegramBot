from flask import Flask, request, jsonify

import uuid
import time
import requests
from config import Config

from utils import redis_client

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add/', methods=['POST'])
def add():
    chat_id = request.form.get('chat_id')
    if redis_client.get(chat_id):
        token = redis_client.get(chat_id).decode('utf-8')
        message = '链接已经存在，无须再次添加\n'
    else:
        token = str(uuid.uuid3(uuid.NAMESPACE_DNS, chat_id + str(int(time.time()))))
        redis_client.set(token, chat_id)
        redis_client.set(chat_id, token)
        message = '您的链接添加成功，使用请使用/help命令.\n'
    url = 'http://' + request.host + '/{}/push/'
    return jsonify({
        'code': 0,
        'message': message,
        'data': {
            'url': url.format(token)
        }
    })


@app.route('/remove/', methods=['POST'])
def remove():
    chat_id = request.form.get('chat_id')

    if redis_client.get(chat_id):
        token = redis_client.get(chat_id)
        redis_client.delete(token.decode('utf-8'))
        redis_client.delete(chat_id)
        message = '您的链接已经移除，原链接不可以使用，可以使用/add指令添加.'
    else:
        message = '链接不存在无须移除.'
    return jsonify({
        'code': 0,
        'message': message,
        'data': {
            'url': None
        }
    })


@app.route('/<token>/push/', methods=['POST'])
def push(token):
    """
    :param chat_id: 聊天ID
    :param text: 文本内容
    :param parse_mode: Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs
    in your bot's message.
    :param disable_web_page_preview: 禁用此消息中链接的链接预览
    :param disable_notification: 无声地发送消息。用户将收到一个没有声音的通知。
    :param reply_to_message_id: 如果消息是回复，则使用原始消息的ID
    :param reply_markup: 额外的接口选项。用于内联键盘、自定义应答键盘、删除应答键盘或强制用户应答的指令的json序列化对象。
    :return:
    """
    if redis_client.get(token):
        chat_id = redis_client.get(token)
        text = request.form.get('text', default='本次消息为空')
        parse_mode = request.form.get('parse_mode', default='')
        disable_web_page_preview = request.form.get('disable_web_page_preview', default=False)
        disable_notification = request.form.get('disable_notification', default=False)
        conn = requests.get(
            url=Config.BOT_SEND_MESSAGE_URL,
            params={
                'text': text,
                'chat_id': chat_id.decode('utf-8'),
                'parse_mode': parse_mode,
                'disable_web_page_preview': disable_web_page_preview,
                'disable_notification': disable_notification
            }
        )
        if conn.json().get('ok'):
            return jsonify({
                'code': 200,
                'message': 'push message success'
            })
        else:
            return jsonify({
                'code': 400,
                'message': 'push message fail'
            })
    else:
        return jsonify({
            'code': 400,
            'message': 'not find'
        })


if __name__ == '__main__':
    app.run()
