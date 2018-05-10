#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import os
#reload(sys)
#sys.setdefaultencoding('utf-8')
import HtmlParse as htParse
from dataBase import *
import cwPythonTogether as cw
import zhihu as webb
def InsertIntoDataBase(spider,spiderdb,type1):
    if type1 == 2:
        for singaldata in spider.pagestory:#从爬出的数据中一条一条提取加入数据库
            if not spiderdb.ExistInDataBase(u"%s" %(singaldata[1]),2):
                spiderdb.writedata = [singaldata[0],singaldata[1]]
                spiderdb.cwdb_add(4)
    if type1 == 3:
        for singaldata in spider.pagestory:#从爬出的数据中一条一条提取加入数据库
            if not spiderdb.ExistInDataBase(int(u"%s" %(singaldata[2])),3):
                spiderdb.writedata = [spider.page,u"%s" %(singaldata[0]),u"%s" %(singaldata[1]),int(u"%s" %(singaldata[2])),spider.type1]
                spiderdb.cwdb_add(3)


def InsertData(startindex,endindex):
    spiderdb = qbdb() 
    spider = htParse.URLPARSE()
    website = ('http://www.ixxzy22.com/?m=vod-index-pg-%s.html',2,3,14) 
    #子爬虫,因为有两种网址要解析
    spiderson = htParse.URLPARSE()
    spiderdb.init_database_type(website[1]) 
    curpage = startindex
    while curpage <= endindex:
        print(u'''当前处理页数:%s''' %(str(curpage))) 
        #指定爬虫要爬取的网址,以及网址的类型
        spider.pagestory = []
        spider.mySite(website[0] %(str(curpage)),website[1])
        for index in range(len(spider.pagestory)):#
            print(u'''当前处理编号:%s''' %(str(index))) 
            spiderson.pagestory = []
            spiderson.mySite(spider.pagestory[index][1],256)
            if(len(spiderson.pagestory) > 0):
                spider.pagestory[index][1] = spiderson.pagestory[0]
            time.sleep(1.5)
        curpage = (curpage + 1)
        #将读取到的数据插入数据库
        InsertIntoDataBase(spider,spiderdb,website[1])
    spiderdb.Showwebsite()
    
def GetWebSite(strname):
    #获取查找内容
    spiderdb = qbdb() 
    spiderdb.init_database_type(2) 
    return spiderdb.findFormTableixxzy(strname)  
if __name__ == '__main__':
    #InsertData(1,55)
    #GetWebSite('撩')
    randopen()