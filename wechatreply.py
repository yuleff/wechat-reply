#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#encoding=utf-8
#function：
#created by xkq
#date: 2018
# -*- coding:utf-8 -*-
import itchat #//导入itchat模块
from itchat.content import *
#二维码登陆网页版微信
itchat.auto_login(hotReload=True)#itchat.auto_login(hotReload=True)参数为True时，避免每次运行都要扫码

apiUrl = 'http://www.tuling123.com/openapi/api'

def get_response(message):
    data = {
    'key':'4715746b938c4aa2bfdef674bd1d30ff',#yes,do as you see
    'info': message,
    'userid' : 'yuleff',
    }


#@itchat.msg_register(itchat.content.TEXT)# //接收微信消息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING,PICTURE, RECORDING, ATTACHMENT, VIDEO])
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING,PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def text_reply1(msg):
    if msg.text:
        #users = itchat.search_friends(name=u'张山')  # 通讯录中好友备注名
        myUserName = itchat.get_friends(update=True)[0]["UserName"]  ##获取自己的username
        #print('myUserName=', myUserName)
        #print('FromUserName=', msg['FromUserName'])  ##获取发消息的好友的username
        remark_name = msg['User']['RemarkName']  ###备注名称
        if msg['Content']:
            itchat.send(u'@%s\u2005: %s  %s \n我是机器人！' % (msg['ActualNickName'], msg['Content'], remark_name), toUserName=msg['FromUserName'])
itchat.auto_login(True) #//登录微信函数(需要扫描二维码),加上True在一定时间内不用每次运行都扫二维码
itchat.run() #//运行