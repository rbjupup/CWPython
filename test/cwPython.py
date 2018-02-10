import time
import random
import bisect
from cwclass import *

from tkinter import *
def show_list():
    mylist = [1,2,3,4]
    mylist.append(5)
    print(mylist)
    
def show_set():
    '''this funtion show you how to create a set'''
    setres = set([1,2,3,4])
    print(setres)
    setres2 = set((1,2,3,4,5))
    print(setres2)
    setresdiff = setres.difference(setres2)
    print(setresdiff)
    '''here have other way there are'''
    '''add +  clear inserstion& issubset<=  isuperset>= remove
        union| symmetric_difference^'''

def show_hash():
    '''this funtion show you how to use hash '''
    help(hash)
    hash(123)
    hash('123') 
    
def show_dictionary():
    highschool = {}
    highschool['wuzenan'] = ['qiaozhong','class 5','class 11']
    highschool['chenweikun'] = ['dazhong','unknow']
    highschool['lurenjia'] = ['luren','luren']
    print(highschool)
    '''del operate'''
    del highschool['lurenjia']
    '''xun huan'''
    for oneperson in highschool:
        print(oneperson,highschool[oneperson])
    '''member'''
    '''clear get key item values update'''
def show_getminmether():
    '''this function show you how to use a lessful algorithm 
    to get min index'''
    count = [8,6,4,7,55,799,454,353,354,745,223]
    low = min(count)
    min_index = count.index(low)
    print('min index is:',min_index)
    
 
#show_searchanndsort start
def serch_liner(v,L):
    '''return first occurrence index or L len'''
    i = 0
    lenL = len(L)
    while i != lenL and L[i] != v:
        i = i+1
    print('index is :',i)
    return i

def serch_liner_index(v,L):
    '''return first occurrence index or L len'''
    i = L.index(v)
    print('index is :',i)
    return i

def serch_liner_for(v,L):
    '''return first occurrence index or L len'''
    for i in L:
        if v == i:
            print(i)
            return i
    return len(L)

def serch_liner_solider(v,L):
    '''return first occurrence index or L len'''
    L.append(v)
    i = 0
    while v != L[i]:
        i = i + 1
    L.pop()
    return i

def serch_binary(v,L):
    '''return first occurrence index or L len'''
    i = 0
    j = len(L) - 1
    while i != j + 1:
        m = (int)((i + j) / 2)
        if L[m] < v:
            i = m + 1
        else:
            j = m - 1
    if 0<=i<len(L) and L[i] == v:
        print(i)
        return i
    else:
        return len(L)
    
def show_sort(L):
    i = 0
    while i != len(L) - 1:
        j = i + 1
        smallest = j
        while j != len(L):
            if(L[j] < L[smallest]):
                smallest = j
            j = j + 1
        L[i],L[smallest] = L[smallest],L[i]
        i = i + 1
        
def show_bubble(L):
    i = len(L)
    while i != 2:
        j = 0
        while j != i - 1:
            if(L[j] > L[j+1]):
                L[j] , L[j + 1] = L[j + 1] , L[j] 
            j = j + 1
        i = i - 1
        
def insertion_sort(L):
    i = 0
    while i != len(L):
        insert(L,i)
        i = i + 1
        
def insert(L,b):
    i = b 
    while i != 0 and L[i - 1] >= L[b]:
        i = i - 1
    value = L[b]
    del L[b]
    L.insert(i,value)
    
def bin_sort(L):
    result = []
    for v in L:
        bisect.insort_left(result,v)
    return result

def show_merge(L):
    result = []
    tmp = []
    
    for onel in L:
        result.append([onel])
    
    while len(result) != 1:    
        for i in range((int)(len(result)/2)):
            tmp.append(merge(result[i],result[-i-1]))
    
        if(len(result) % 2 != 0):    
            tmp.append(result[(int)(len(result)/2)+1])
        
        result = tmp
        tmp = []
    return result
        
    
    
def merge(L1,L2):
    i = 0
    j = 0
    result = []
    while i != len(L1) and j != len(L2):
        if(L1[i] <= L2[j]):
            result.append(L1[i])
            i  = i + 1
        else:
            result.append(L2[j])
            j = j + 1
    result.extend(L1[i:])
    result.extend(L2[j:])
    
    return result

def smile(way1 = 'haha',way2 = 'xixi'):
    print(way1,way2)
    raise ValueError("just a joy")
    
def out_max(*value):
    if not value:
        return None
    m = value[0]
    for v in value[1:]:
        if v > m:
            m = v
    return m

class Color(object):
    r = 0
    g = 0
    b = 0
    def init_white(self):
        self.r = 255
        self.b = 255
        self.g = 255
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
    def __add__(self,other):
        return Color(self.r + other.r,
        self.g + other.g,
        self.b + other.b)
class CwColor(Color):
    pass
def show_color():
    red = Color(255,0,0)
    white = Color(0,0,0)
    white.init_white()
    red = red + white
    print(red.g)

def GUI_program():
    window = Tk()
    label = Label(window,text = "hello wrold")
    label.pack()
    window.mainloop()
#show_searchanndsort end
    
def show_time():
    '''import time at first'''
    time_start=time.time()
    cwclass.var_label_example()
    time_end=time.time()
    print('totally cost',time_end-time_start)   

if __name__ == '__main__':
    show_time()
    
    
#import nose
#if __name__ == '__main__':
#    nose.runmodule()