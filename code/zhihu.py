#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dataBase import *

from cwPythonTogether import *
#spiderdb = qbdb() 
#spiderdb.init_database_type(5)   
#books = spiderdb.GetBook('机器学习',1)
#myset = set(books)
#print(len(myset))
#for item in myset:
    #print("%s    %d 次" %(item, books.count(item)))
#html_doc = Cwfile().Load("D:\\warmdata\\testtxt\\zhihujiqixuexi.txt")
#spiderdb = qbdb() 
#spiderdb.init_database_type(5)   
#for sindata in html_doc:
    #spiderdb.writedata = []
    #spiderdb.writedata.append('机器学习')
    #spiderdb.writedata.append(sindata)
    #spiderdb.cwdb_add(5)   
    #print(sindata)
#books = spiderdb.GetBook('机器学习',1)
#myset = set(books)
#print(len(myset))
#for item in myset:
    #print("%s    %d 次" %(item, books.count(item)))

def GetZhihuLinkType(valink):
    #知乎的link分为问题和专栏和主题
    zhuanlan = 'https://zhuanlan.zhihu.com(.*)'    
    question = 'https://www.zhihu.com/question/(.*)' 
    if len(find_use_re(valink,zhuanlan)) > 0:
        return 1
    if len(find_use_re(valink,question)) > 0:
        return 2    
    return 0
        


def getcommentFromLink(browser,valink):
    linkType = GetZhihuLinkType(valink)
    if linkType == 0:
        return []
    browser.get(valink)
    try:
        if linkType == 2:
            #点显示全部//*[@id="root"]/div/main/div/div[2]/div[1]/div[1]/a
            a = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div[1]/div[1]/a')
            WebDriverWait(browser,2,0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/main/div/div[2]/div[1]/div[1]/a')))
            ActionChains(browser).click(a).perform()
            for x in range(500):
                ActionChains(browser).send_keys(Keys.DOWN).perform()                
            #获取全部答案
            bpath = '//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div/div'
            b = browser.find_elements_by_xpath(bpath)
            WebDriverWait(browser,1,0.5).until(EC.visibility_of_element_located((By.XPATH,bpath)))    
            #单个获取评论放到容器里面
            resdata = []
            print(len(b))
            if len(b) > 1:
                for sincommentIndex in range(len(b)-1):
                    try:
                        chilecomment = b[sincommentIndex].find_elements(By.CLASS_NAME,'RichText')
                        if len(chilecomment) > 0:
                            data = chilecomment[-1].text
                            resdata.append(data)
                    except Exception as e: 
                        print('err')            
            return resdata 
        if linkType == 1:
                for x in range(500):
                    ActionChains(browser).send_keys(Keys.DOWN).perform()        
                #单个获取评论放到容器里面
                resdata = []
                chilecomment = browser.find_elements(By.XPATH,'//*[@id="root"]/div/main/div/article/div[1]/div/p')
                if chilecomment == None:
                    chilecomment = browser.find_elements(By.XPATH,'//*[@id="root"]/div/main/div/article/div[1]/div/h2')
                if chilecomment != None:
                    for sinLine in chilecomment:
                        resdata.append(sinLine.text)
                return resdata
    except Exception as e:
        return []




def GetzhihuBook(e):
    spiderdb = qbdb() 
    spiderdb.init_database_type(5)       
    books = spiderdb.GetBook(e,1)
    if len(books) > 0:
        myset = set(books)
        print("-----------------------------------------\n")
        print("-----------查找完成,共找到书%d本-----------\n" %(len(myset)))
        booksset = {}
        for item in myset:
            booksset[item] = books.count(item)
        #print(booksset)
        resbookset = sorted(booksset.items(),key = lambda x:x[1],reverse = True)
        for item ,num in resbookset:
            print("%s    %d 次" %(str(item), num))
        return 

        
        
    url = 'https://www.zhihu.com/explore'
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(url)
    
    ##登录帐号,点击登录。
    #a = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span')
    #WebDriverWait(browser,15,0.6).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span')))
    #ActionChains(browser).click(a).perform()
    
    ##定位二维码登录。
    #b = browser.find_element_by_xpath('//button[@class="Button Button--plain"]')
    #WebDriverWait(browser,15,0.7).until(EC.visibility_of_element_located((By.XPATH,'//button[@class="Button Button--plain"]')))
    #ActionChains(browser).click(b).perform()
    #time.sleep(15)
    ##登录后查询关键词
    #定位
    c = browser.find_element_by_link_text('发现')
    WebDriverWait(browser,17,0.7).until(EC.presence_of_element_located((By.LINK_TEXT,'发现')))
    ActionChains(browser).click(c).perform()
    
    #点击搜索输入框
    d = browser.find_element_by_xpath('//*[@id="q"]')
    WebDriverWait(browser,15,0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="q"]')))
    ActionChains(browser).click(d).perform()
    
    ActionChains(browser).send_keys(e).perform()
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    #拉动滚动条到最底部
    for x in range(5000):
        ActionChains(browser).send_keys(Keys.DOWN).perform()
    #获取所有的标题及链接
    url_list = browser.find_elements_by_xpath('//div[@class="List-item"]//a')
    title_list = browser.find_elements_by_xpath('//div[@class="List-item"]//a/span[@class="Highlight"]')
    
    info_dict = {}
    for k,v in zip(url_list,title_list):
        urls = k.get_attribute('href')
        titles = v.text
        info_dict[titles] = urls
    
    print(info_dict)
    #写入文本文档
    resultdata = []
    curprocess = 0
    for ka,va in info_dict.items():
        print("正在处理%s/%d\n"%(str(curprocess),len(info_dict))) 
        tmpdata = getcommentFromLink(browser,va)
        if tmpdata != None:
            for sindata in tmpdata:
                resultdata.append(sindata) 
                print(sindata)        
        curprocess += 1
    browser.quit()
    
    print('网页数据获取完成')
    print(resultdata)
    
    

    for sindata in resultdata:
        spiderdb.writedata = []
        spiderdb.writedata.append(e)
        spiderdb.writedata.append(sindata)
        spiderdb.cwdb_add(5)   
    books = spiderdb.GetBook(e,1)
    if len(books) > 0:
        myset = set(books)
        print("-----------------------------------------\n")
        print("-----------查找完成,共找到书%d本-----------\n" %(len(myset)))
        booksset = {}
        for item in myset:
            booksset[item] = books.count(item)
        #print(booksset)
        resbookset = sorted(booksset.items(),key = lambda x:x[1],reverse = True)
        for item ,num in resbookset:
            print("%s    %d 次" %(str(item), num))
        return 

def openweb(site):
    url = site
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(url)    

def randopen():
    spiderdb = qbdb() 
    spiderdb.init_database_type(2) 
    website =  spiderdb.GetRandomOne()  
    openweb(website)    
         
#randopen()   
#e = input('请输入你要查询的内容：')
#GetzhihuBook(e)