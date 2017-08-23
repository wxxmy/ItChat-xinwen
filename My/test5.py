# coding-utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import itchat


def my_job():
    msg = '您好，现在时间是 %s' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    itchat.send(msg, toUserName='@@eb4ee16e977579e70702cc7d1afad36dbe4cbf961b0c0ef6e546ae9cc01466dc')

itchat.auto_login(hotReload=True)
sched = BlockingScheduler()


# 每隔5秒运行一次my_job1
sched.add_job(my_job, 'interval', seconds=5, id='my_job')

sched.start()
#itchat.run()
