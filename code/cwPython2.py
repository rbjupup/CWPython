#!/usr/bin/env python
# -*- coding: utf-8 -*-
#输入上面那段之后就可以输入汉字了,神奇
import re
import nose

def find_use_re(Content,strre):
    '''这个函数输入字符串和正则,将匹配到的结果输出出来'''
    Petterm = re.compile(strre, re.S)
    param = re.findall(Petterm, Content)    
    return param
def test_findre():
    '''测试正则匹配'''
    strfinded = '123(.*?)678' 
    L = find_use_re('12345678',strfinded)
        

def main():
    pass

if __name__ == "__main__":
    #nose.runmodule()
    main()