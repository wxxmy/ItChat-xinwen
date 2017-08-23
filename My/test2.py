from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import itchat
import time


#def my_job1():
    #itchat.send('my_job1 is running, Now is %s' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def group_reply_text(msg):
    #time.sleep(2)
    reply_text = msg['Text']
    if msg['Text'] == '时间':
        itchat.send('现在时间 %s' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), msg['FromUserName'])
    elif msg['Text'] == '你是谁':
        return '这不重要'
    return

itchat.auto_login(hotReload=True)
itchat.run()





# 获取所有通讯录中的群聊
# 需要在微信中将需要同步的群聊都保存至通讯录
#chatrooms = itchat.get_chatrooms(update=True, contactOnly=True)
#chatroom_ids = [c['UserName'] for c in chatrooms]