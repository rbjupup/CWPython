#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cwPython2
import cwPythonTogether as cw
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

import urllib
import urllib2
import re
from bs4 import BeautifulSoup


class URLPARSE:
    '''这个类用来解析静态的网站,返回从该网址提取的资源,目前支持的网址类型有糗百而已
    输入网址类型,网址,然后会获得数据,并类似点击下一页那样,然后将获得的数据打包返回'''
    def __init__(self):
        self.page = 1
        self.type = 1
        self.useragent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.useragent}
        self.stories = []
        self.pagestory = []
        self.Enable = True
        self.url = 'http://www.qiushibaike.com/hot/page/'

    def RenewUrl(self):
        if self.type == 1:
            self.url = 'http://www.qiushibaike.com/hot/page/' + str(self.page)
            self.page += 1
     
    def mySite(self,newurl,newtype):
        self.url = newurl
        self.type = newtype
        #爬虫开始爬
        self.Loading2Start()
    
    def LoadPage(self, page):
        #try:
            Request = urllib2.Request(self.url, headers=self.headers)
            Responese = urllib2.urlopen(Request)
            PageOutput = Responese.read().decode('utf-8')
            return PageOutput

        #except urllib2.URLError,e:
            #if hasattr(e, 'reason'):
                #print '连接到糗事百科失败，失败原因:', e.reason
                #return None
    
    def DealOfHtml(self,Content):
        if self.type == 1:
            #print(Content)
            soup = BeautifulSoup(Content, features="lxml")
            tags = soup.find_all(name='div', attrs={'class': 'content'})
            goods = soup.find_all(name='span', attrs={'class': 'stats-vote'})
            authors = soup.find_all(name='div', attrs={'class': 'author clearfix'})
            findres = []
            for duanziindex in range(len(tags)):
                authorname = authors[duanziindex].select('h2')[0].get_text('h2')
                contantsingal = tags[duanziindex].select('span')[0].get_text('span')
                contantsingal = contantsingal.replace('span',' ')
                goodssingal = goods[duanziindex].select('i')[0].get_text('i')
                self.pagestory.append([cw.get_str(authorname,"\""),cw.get_str(contantsingal,"\""),cw.get_str(goodssingal,"\"")])
        elif self.type == 2:
            soup = BeautifulSoup(Content, features="lxml")
            singalweb = soup.find_all(name='span', attrs={'class': 'xing_vb4'})
            for webindex in range(len(singalweb)):
                Titlename = singalweb[webindex].select('a')[0].get_text('a')
                websitetmp = singalweb[webindex].select('a')[0].get('href')
                website = '''http://www.ixxzy22.com'''+websitetmp
                self.pagestory.append([Titlename,website])
        elif self.type == 256:
            #print(Content)
            soup = BeautifulSoup(Content, features="lxml")
            singalweb = soup.find_all(name='', attrs={'name': 'copy_sel'})
            for webindex in range(len(singalweb)):
                websitetmp = singalweb[webindex].get('value')
                website = '''http://www.ixxplayer.com/video.php?url='''+websitetmp
                self.pagestory.append(website)                  
                    
            
    def NeedStop(self):
        '''这个函数判断是否需要停止'''
        if self.type == 1:
            if len(self.pagestory) >= 3:#假如收集到了上百个笑话就退出
                return True
        return False
         
    def GetPageItem(self, page):
        Content = self.LoadPage(self.page)
        #print(Content)
        if not Content:
            print('error')
            return None
        #cw.Cwfile().save_to_file('contant%s.txt' %(str(self.page)),Content)
        self.DealOfHtml(Content)

    def ShowResult(self):
        '''测试用的,将获得的结果显示出来'''
        if self.type == 1:
            for singalData in self.pagestory:
                text = u"第%s页\t作者:%s\n%s\n点赞数:%s" % (
                    self.page, singalData[0], singalData[1], singalData[2])
                print("+------------------------------+")
                print(text)
                print("+------------------------------+")
        
        

    def Loading2Start(self):
        self.GetPageItem(self.page)

#if __name__ == '__main__':
    #spider = URLPARSE()
    #spider.mySite('http://www.qiushibaike.com/hot/page/'+str(spider.page),1)
    #spider.Loading2Start()
    #spider.ShowResult()    


