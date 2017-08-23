# coding-utf-8
import requests
from bs4 import BeautifulSoup
import SinaNews
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import itchat

def main():
    #主函数,抓取新浪新闻
    url='http://news.sina.com.cn/china/'
    ct=requests.get(url)
    ct.encoding="UTF-8"
    #构建soup对象
    manSoup=BeautifulSoup(ct.text,"html.parser")
    #获取新闻列表
    newsItems=manSoup.select(".news-item")
    #遍历新闻
    count = 1
    newsAll = ""
    for item in newsItems:
        h2=item.select("h2")
        if(len(h2)>0):
            a=h2[0].select("a")[0]
            a_text=a.text;
            a_href=a["href"];
            newinstance=SinaNews.getnews(a_href)
            news = str(count)+"."+newinstance.title+"\r\n"
            newsAll+=news
            #print(news)
            count += 1
            if count == 20:
                return newsAll

def my_job():
    msg1 = '您好，现在时间是 %s' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\r\n'
    msg2 = main()
    msg = msg1 + msg2
    itchat.send(msg, toUserName='@@930e45b8953e36b273ef8cd52d75f6954cc3bc0e79a48a31fadc560c0cee8434')

itchat.auto_login(hotReload=True)
sched = BlockingScheduler()


# 每隔5秒运行一次my_job1
sched.add_job(my_job, 'interval', seconds=30, id='my_job')

sched.start()
#itchat.run()






