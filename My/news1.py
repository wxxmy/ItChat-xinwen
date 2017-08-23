# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import SinaNews



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
            news = str(count)+"."+newinstance.title+"\r\n发布时间："+ newinstance.publishtime
            newsAll+=news
            #print(news)
            count += 1
            if count == 20:
                break
    return newsAll

msg=main()
print(msg)
