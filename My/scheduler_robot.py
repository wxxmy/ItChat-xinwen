from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import itchat


def my_job1():
    itchat.send('my_job1 is running, Now is %s' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


sched = BlockingScheduler()


@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def text_reply(msg):
    # 每隔5秒运行一次my_job1
    sched.add_job(my_job1, 'interval', seconds=5, id='my_job1')

sched.start()

itchat.auto_login(hotReload=True)
itchat.run()





# 获取所有通讯录中的群聊
# 需要在微信中将需要同步的群聊都保存至通讯录
#chatrooms = itchat.get_chatrooms(update=True, contactOnly=True)
#chatroom_ids = [c['UserName'] for c in chatrooms]