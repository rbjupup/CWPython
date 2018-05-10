#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''这个程序用来做爬虫'''
    #初始化数据库
    #插入初始化网址
    #开始提取数据库数据,判断是不是没有爬过
    #判断下网址的类型
    #对网址进行数据提取
    #将提取的数据输入数据库
    
import sys
import time
import os
reload(sys)
sys.setdefaultencoding('utf-8')
import HtmlParse as htParse
from dataBase import *    




def getQiuBai():
    spiderdb = qbdb() 
    spider = htParse.URLPARSE()
    qiubaiType = [('http://www.qiushibaike.com/textnew/page/%s',1,3,14),
                  ('http://www.qiushibaike.com/text/page/%s',1,3,14),
                  ('http://www.qiushibaike.com/hot/page/%s',1,3,14)]
    for sinTask in qiubaiType:
        spiderdb.init_database_type(sinTask[1]) 
        curpage = 1
        while curpage <= 35:
            #指定爬虫要爬取的网址,以及网址的类型
            spider.mySite(sinTask[0] %(str(curpage)),1)
            #将读取到的数据插入数据库
            InsertIntoDataBase(spider,spiderdb,sinTask[2])
            curpage += 1    
            print('''当前处理页数:''') 
            print(curpage)
            time.sleep(0.5)        
        spiderdb.ShowTopTen()
        return


    
#正式框架,输入网址,然后将提取数据放到数据库
def GetDataFromWebsite(L,dbType,siteType,sleepTime):
    spiderdb = qbdb() 
    spider = htParse.URLPARSE()
    spiderdb.init_database_type(dbType)  
    curpage = 0
    for site in L:
        #指定爬虫要爬取的网址,以及网址的类型
        spider.mySite(site,siteType)
        #将读取到的数据插入数据库
        InsertIntoDataBase(spider,spiderdb,dbType)
        curpage += 1    
        print('''当前处理页数:%d''' %(str(curpage))) 
        time.sleep(sleepTime) 
        
#正式框架,插入到数据库
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
                

#正式框架,插入到数据库
def GetWebSite(getWay):
    pass

#正式框架,查询结果
def GetResult(GetWhat):
    pass

def main():
    pass

if __name__ == '__main__':
    main()