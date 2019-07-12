# -*- coding=utf-8 -*-
import requests
import itchat
import random
#二维码登陆网页版微信
itchat.auto_login(hotReload=True)#itchat.auto_login(hotReload=True)参数为True时，避免每次运行都要扫码
KEY = '4715746b938c4aa2bfdef674bd1d30ff'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots=[]
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply

itchat.auto_login(enableCmdQR=True)
itchat.run()
