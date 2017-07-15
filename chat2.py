import itchat
import tuling
from itchat.content import *

r=[]

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    #itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

    if msg['FromUserName'] in r:
        t='（来自Python脚本的智能回复）'+tuling.get_rpl(msg['Text'])
        itchat.send(t,msg['FromUserName'])
    else:
        if msg['Text']=="智能聊天":
            r.append(msg['FromUserName'])
            itchat.send('（来自Python脚本的自动回复）已开启智能回复模式',msg['FromUserName'])
        else:
            itchat.send('（来自Python脚本的自动回复）本人学习中，暂时无法回复，有事请留言',msg['FromUserName'])
            itchat.send('（来自Python脚本的自动回复）输入：智能聊天，开启智能回复模式',msg['FromUserName'])

            
itchat.auto_login()
itchat.run()
