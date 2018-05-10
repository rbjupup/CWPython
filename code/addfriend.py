#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cwPythonTogether as cw
shouji = '//*[@id="qlogin_tips_1"]/a'
erweima = '//*[@id="qr_area"]/span[1]'
erweima75 = '//*[@id="img_out_755163440"]'
friend = '//*[@id="tb_friend_li"]'
findfriend = '//*[@id="friends-drop-down"]/div[1]/div[1]/a[2]'
url = 'https://user.qzone.qq.com'
baiduinput = '//input[@id="kw"]'
groupf = '//*[@id="menu-list"]/li[2]/a'
allgroup = '//*[@id="menu-group-ul"]/li'
addas = '/html/body/div[14]/div/div/div[3]/div/div[1]'
addlin = '//*[@id="qun_fuin_10453926"]/div[2]/div[1]/a'
startgroup = 0
startmem = 11

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(url)
#跳转到frame中,新知识
browser.switch_to_frame('login_frame')
a = browser.find_element_by_xpath(shouji)
WebDriverWait(browser,15,0.5).until(EC.visibility_of_element_located((By.XPATH,shouji)))
b = browser.find_element_by_xpath(erweima75)
if(EC.visibility_of_element_located((By.XPATH,erweima75))):
    ActionChains(browser).click(b).perform()
browser.switch_to.default_content()

c = browser.find_element_by_xpath(friend)
WebDriverWait(browser,15,0.5).until(EC.visibility_of_element_located((By.XPATH,friend)))
ActionChains(browser).move_to_element(c).perform()  

d = browser.find_element_by_xpath(findfriend)
WebDriverWait(browser,15,0.5).until(EC.visibility_of_element_located((By.XPATH,findfriend)))
ActionChains(browser).click(d).perform()  
time.sleep(3)

elementi= browser.find_element_by_class_name('app_canvas_frame')
browser.switch_to_frame(elementi) 
e = browser.find_element_by_xpath(groupf)
WebDriverWait(browser,15,0.5).until(EC.visibility_of_element_located((By.XPATH,groupf)))
ActionChains(browser).click(e).perform()   
time.sleep(2)

url_list = browser.find_elements_by_xpath(allgroup)
for singroup in url_list:
    chilegroup = singroup.find_element(By.CLASS_NAME,'item-con')
    qunid = chilegroup.get_attribute("data-qunid")
    ActionChains(browser).click(singroup).perform()
    time.sleep(2)    
    #f = browser.find_elements(By.CLASS_NAME,'gb_bt')#"//*[start-with(@id,'qun_btn')]"
    f = browser.find_elements(By.CLASS_NAME,'nickname')
    print(len(f))
    for addone in f:
        str1 = addone.get_attribute("href")
        str2 = 'https://user.qzone.qq.com/(.*)'
        numres = cw.find_use_re(str1,str2)      
        print("%s----%s----%s" %(qunid,addone.text,numres[0]))
        #ActionChains(browser).click(addone).perform()  
        #time.sleep(3)
        #browser.switch_to.default_content()
        #g = browser.find_element_by_xpath(addas)
        #WebDriverWait(browser,15,0.5).until(EC.visibility_of_element_located((By.XPATH,addas)))
        #ActionChains(browser).click(g).perform() 
        #time.sleep(0.5) 
        #elementi= browser.find_element_by_class_name('app_canvas_frame') 
        #browser.switch_to_frame(elementi) 
        #time.sleep(1)
time.sleep(1000)