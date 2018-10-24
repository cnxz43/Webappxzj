import itchat
import requests

# itchat.auto_login()
#
# itchat.send('Hello, filehelper', toUserName='filehelper')

# import itchat
#
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # msg.user.send()
    return msg.text

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, "甜甜绝世大笨蛋"))

itchat.auto_login()
itchat.run()