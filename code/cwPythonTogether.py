#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import nose

import time
import random
import bisect
import cwPython2 as rbj
from bs4 import BeautifulSoup

    
def find_use_re(Content,strre):
    '''这个函数输入字符串和正则,将匹配到的结果输出出来'''
    Petterm = re.compile(strre, re.S)
    param = re.findall(Petterm, Content)    
    return param
def test_findre():
    '''测试正则匹配'''
    strfinded = '<div class="author.*?<h2>(.*?)</h2>\n.*?<span>(.*?)</span>\n\n\n</div>(.*?)<div class="stats">\n<span class="stats-vote"><i class="number">(.*?)</i>' 
    html_doc = Cwfile().Load("D:\\warmdata\\testtxt\\qiubai.txt")
    L = find_use_re(html_doc,strfinded)
    for oneline in L:
        print(oneline)

def beautifulsoup_QiuBai():
    html_doc = Cwfile().Load("D:\\test.txt")
    soup = BeautifulSoup(html_doc, features="lxml")
    tags = soup.find_all(name='div', attrs={'class': 'content'})
    goods = soup.find_all(name='span', attrs={'class': 'stats-vote'})
    authors = soup.find_all(name='div', attrs={'class': 'author clearfix'})
    findres = []
    for duanziindex in range(len(tags)):
        authorname = authors[duanziindex].select('h2')[0].get_text('h2')
        contantsingal = tags[duanziindex].select('span')[0].get_text('span')
        goodssingal = goods[duanziindex].select('i')[0].get_text('i')
        findres.append([authorname,contantsingal,goodssingal])
    
    for singalres in  findres:
        print(singalres[0])
        print(singalres[1])
        print(singalres[2])
    print(len(tags))
    print(len(goods))
    print(len(authors))
def beautifulsoup_ixxzy(type):
    if type == 1:
        html_doc = Cwfile().Load("D:\\warmdata\\testtxt\\testixxzy.txt")
        soup = BeautifulSoup(html_doc, features="lxml")
        singalweb = soup.find_all(name='span', attrs={'class': 'xing_vb4'})
        findres = []
        for webindex in range(len(singalweb)):
            Titlename = singalweb[webindex].select('a')[0].get_text('a')
            websitetmp = singalweb[webindex].select('a')[0].get('href')
            website = '''http://www.ixxzy22.com'''+websitetmp
            findres.append([websitetmp,website])        
    elif type ==2:
        html_doc = Cwfile().Load("D:\\warmdata\\testtxt\\testGetm3u8.txt")
        soup = BeautifulSoup(html_doc, features="lxml")
        singalweb = soup.find_all(name='', attrs={'name': 'copy_sel'})
        #for singal in singalweb:
            #print(singal)
        findres = []
        for webindex in range(len(singalweb)):
            websitetmp = singalweb[webindex].get('value')
            website = '''http://www.ixxplayer.com/video.php?url='''+websitetmp
            print(website)
            findres.append([website])            

    
def beautifulsoup():
    html_doc = Cwfile().Load("D:\\test.txt")
    soup = BeautifulSoup(html_doc, features="lxml")
    # 找到第一个a标签
    tag1 = soup.find(name='a')
    print(tag1.name)
    # 找到所有的a标签
    tag2 = soup.find_all(name='a')
    print(tag2)
    # 找到id＝link2的标签
    tag3 = soup.select('#link2')   
    
    tag = soup.find('a')
    name = tag.name # 获取
    print(name)
    tag.name = 'span' # 设置
    print(soup)  
    tag = soup.find('a')
    attrs = tag.attrs    # 获取
    print(attrs)
    tag.attrs = {'ik':123} # 设置
    tag.attrs['id'] = 'iiiii' # 设置
    print(soup)    
    
    
class Cwfile():
    def Load(self,filepath):
        try:
            f = open(filepath,'r', encoding='UTF-8')
            contents = []
            for line in f.readlines():
                contents.append(line.strip()) # 把末尾的'\n'删掉
            f.close()   
            return contents
        finally:
            if f:
                f.close()        
        
    def save_to_file(self,filename,data):
        f = open(filename, 'w+')
        f.writelines(data)  
        f.close()
        
def get_str(oriStr,splitStr):
    str_list = oriStr.split(splitStr)
    if len(str_list) > 1:
        for index in range(1, len(str_list)):
            if str_list[index] != '':
                str_list[index] = str_list[index]
            else:
                continue
        return ''.join(str_list)
    else:
        return oriStr
        
def randone(maxval):
    return random.randint(0,maxval)
def show_time():
    '''函数计时'''
    time_start=time.time()
    str1 = 'https://user.qzone.qq.com/18316739'
    str2 = 'https://user.qzone.qq.com/(.*)'
    print(find_use_re(str1,str2))
    time_end=time.time()
    print('totally cost',time_end-time_start)   

if __name__ == '__main__':
    show_time()
    
#import nose
#if __name__ == '__main__':
   #nose.runmodule()