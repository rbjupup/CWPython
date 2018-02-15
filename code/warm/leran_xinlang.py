# coding:UTF-8作者：Python程序员
#链接：https://zhuanlan.zhihu.com/p/30046989
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import requests
import json

headers = {
    'Cookie':'xxxxxxxx',
    'User_Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

f = open('D:/test/weibo.txt','a+',encoding='utf-8')

def get_info(url,page):
    html = requests.get(url,headers=headers)
    json_data = json.loads(html.text)
    card_groups = json_data[0]['card_group']
    for card_group in card_groups:
        f.write(card_group['mblog']['text'].split(' ')[0]+'\n')

    next_cursor = json_data[0]['next_cursor']

    if page<50:
        next_url = 'https://m.weibo.cn/index/friends?format=cards&next_cursor='+str(next_cursor)+'&page=1'
        page = page + 1
        get_info(next_url,page)
    else:
        pass
        f.close()

if __name__ == '__main__':
    url = 'https://m.weibo.cn/index/friends'
    get_info(url,1)