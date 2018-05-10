#import pywifi
#import time
#import const

#wifi = pywifi.PyWiFi()

#iface = wifi.interfaces()[0]

#iface.disconnect()
#time.sleep(1)
#assert iface.status() in\
    #[const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

#profile = pywifi.Profile()
#profile.ssid = 'testap'
#profile.auth = const.AUTH_ALG_OPEN
#profile.akm.append(const.AKM_TYPE_WPA2PSK)
#profile.cipher = const.CIPHER_TYPE_CCMP
#profile.key = '12345678'

#iface.remove_all_network_profiles()
#tmp_profile = iface.add_network_profile(profile)

#iface.connect(tmp_profile)
#time.sleep(30)
#assert iface.status() == const.IFACE_CONNECTED

#iface.disconnect()
#time.sleep(1)
#assert iface.status() in\
#[const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
import pywifi
from pywifi import *
import time
import sys 

profile = pywifi.Profile()
profile.ssid = 'USER_9A28AB'
profile.auth = const.AUTH_ALG_SHARED
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = '00000000'

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
profile = iface.add_network_profile(profile)
iface.connect(profile)
#初始化状态码，考虑到用0会发生些逻辑错误
code = 10
t1 = time.time()
#循环刷新状态，如果置为0则密码错误，如超时则进行下一个
ts = 30
while code!=5 :
    time.sleep(0.1)
    code = iface.status()
    now = time.time()-t1
    if now>ts:
        break
    i = 1
    showID = 'chuncao'
    now = 0.2
    key = 'a888888888'
    sys.stdout.write("\r%-*s| %-*s| %s |%*.2fs| %-*s |  %-*s %*s"%(6,i,18,showID,code,5,now,7,showID,10,i,10,key.replace("\n","")))

