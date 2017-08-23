from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

def my_job1():
    print ('my_job1 is running, Now is %s' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


sched = BlockingScheduler()
# 每隔5秒运行一次my_job1
sched.add_job(my_job1, 'interval', seconds=5,id='my_job1')

sched.start()