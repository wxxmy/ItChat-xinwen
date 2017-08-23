# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

class SinaNews:
    '新浪新闻基类'
    def __init__(self,title):
        self.title=title


def getnews(url):
    ret=requests.get(url)
    ret.encoding="UTF-8"
    soup=BeautifulSoup(ret.text,"html.parser")
    #获取标题
    title=soup.select("#artibodyTitle")[0].text
    #获取内容
    #content=soup.select("#artibody")[0].text
    #获取发布时间
    #pttime=soup.select("#navtimeSource")[0].text;
    return SinaNews(title=title)