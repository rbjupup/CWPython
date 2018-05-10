# -*- coding: utf-8 -*-
#这是用3.5写的
import time
import itchat  
import requests  
from qqbot import _bot as bot
  
from dataBase import *
def GetWebSite1(strname):
    #获取查找内容
    spiderdb = qbdb() 
    spiderdb.init_database_type(2) 
    return spiderdb.findFormTableixxzy(strname)  

def lc():
    print("Finash Login!")
def ec():
    print("exit")

def firsttest():
    itchat.auto_login(loginCallback=lc, exitCallback=ec)
    time.sleep(0.1)
    itchat.send("Hello World!")#回复
    itchat.send("Hello","纯")
    itchat.send_msg("Hello World!")#发送
    itchat.send_msg("Hello","纯")
    itchat.logout()    #强制退出登录 
curnum = 0
totalnum = 0
data = []
def get_response(_info):  
    global data
    global totalnum
    global curnum
    listcomment = _info.split("--")
    if(len(listcomment) != 0):
        if( 'sex' == listcomment[0]):
            data = GetWebSite1(listcomment[1])
            totalnum = len(data)
            curnum = 0
            if(totalnum > 0):
                return {'text':data[0]+":"+data[1]}
    if(len(listcomment) != 0):
        if( 'next' == listcomment[0]):
            curnum = curnum + 1
            if(totalnum > curnum*2):
                return {'text':data[curnum*2]+":"+data[curnum*2+1]}
    print(_info)                                       # 从好友发过来的消息  
    api_url = 'http://www.tuling123.com/openapi/api'   # 图灵机器人网址  
    data = {  
        'key': '485712b8079e44e1bc4af10872b08319',     # 如果这个 apiKey 如不能用，那就注册一次  
        'info': _info,                                 # 这是我们从好友接收到的消息 然后转发给图灵机器人  
        'userid': 'wechat-robot',                      # 这里你想改什么都可以  
    }  
    r = requests.post(api_url, data=data).json()       # 把data数据发  
    print(r.get('text'))                               # 机器人回复给好友的消息  
    return r  

@itchat.msg_register(itchat.content.TEXT)  
def text_reply(msg):  
    return get_response(msg["Text"])["text"]

def wechatautoreply():
    itchat.auto_login(hotReload=True)                  # hotReload = True, 保持在线，下次运行代码可自动登录  
    itchat.run()  
    
if __name__ == '__main__':  
    wechatautoreply()
    
 
    
#def sendMsgToGroup(msg,groupList,bot):
    #for group in groupList:
        #bg=bot.List('group', group)
        #if bg is not None:
            #bot.SendTo(bg[0],msg)

#def sendMsgToBuddy(msg,buddyList,bot):
    #pass

#def main(bot):
    #groupMsg='加好友'
    #buddyMsg='hi'
    #with open('./qq.txt','r') as fr:
        #qqGroup=fr.readline().strip()
        #qqBuddy=fr.readline().strip()
    #qqGroupList=qqGroup.split(',')
    #qqBuddyList=qqBuddy.split(',')
    #sendMsgToGroup(groupMsg,qqGroupList,bot)
    #sendMsgToBuddy(buddyMsg,qqBuddyList,bot)

#if __name__=='__main__':
    #bot.Login(['-q', '75513440'])
    #bot.SendTo(95934243,'hellowrold')
    #bot.send('group',95934243,'hellowrold')
    #main(bot) 