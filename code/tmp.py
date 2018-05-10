# coding:utf-8  
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options) # 选择Chrome浏览器


#username = "18813754497" # 请替换成你的用户名
#password = "A123123a" # 请替换成你的密码
#driver.get('http://vip.jd.com') # 打开京东会员网站
#time.sleep(1)
#driver.find_element_by_link_text('账户登录').click() # 点击“账户登录”
#driver.find_element_by_id('loginname').click() # 点击用户名输入框
#driver.find_element_by_id('loginname').send_keys(username) # 自动敲入用户名
#driver.find_element_by_id('nloginpwd').click() # 点击密码输入框
#driver.find_element_by_id('nloginpwd').send_keys(password) # 自动敲入密码
#driver.find_element_by_id('loginsubmit').click() # 点击“登录”按钮
#time.sleep(1)
#driver.find_element_by_id('signIn').click() # 点击“签到”
userbname = '18813754497'
userpsw = 'A123123a'
serchata = '数学'

driver.get('https://www.zhihu.com/')
time.sleep(100)
loginlink = '//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span'
loginname = '//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input'
loginpsw = '//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input'
loginbutton = '//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button'
sousuo = '//*[@id="root"]/div/div[2]/header/div/div[1]/div/form/div/div/div'
askbutton = '//*[@id="root"]/div/div[2]/header/div/div[1]/button'
pathserch = 'https://www.zhihu.com/search?type=content&q=hello'


driver.find_element_by_xpath(loginlink).click() # 点击“账户登录”
time.sleep(1)
driver.find_element_by_xpath(loginname).click() # 点击用户名输入框
driver.find_element_by_xpath(loginname).send_keys(userbname) # 点击用户名输入框
driver.find_element_by_xpath(loginpsw).click() # 点击密码输入框
driver.find_element_by_xpath(loginpsw).send_keys(userpsw) # 点击密码输入框
time.sleep(1)
driver.find_element_by_xpath(loginbutton).click() # 点击登陆
#time.sleep(5)
#driver.get(pathserch)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,sousuo)))
driver.get(pathserch)
element = wait.until(EC.element_to_be_clickable((By.XPATH,sousuo)))
pageSource = driver.page_source
print(pageSource)

#driver.find_element_by_xpath(sousuo).click() # 点击提问输入框
#driver.find_element_by_xpath(sousuo).send_keys(serchata) # 点击提问输入框
#driver.find_element_by_xpath(askbutton).click() # 点击提问
#driver.close()