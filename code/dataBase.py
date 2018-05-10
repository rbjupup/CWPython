# -*- coding: utf-8 -*-
import sqlite3 as dbapi
import sys
import os
import cwPythonTogether as cw
import random
#reload(sys)
#sys.setdefaultencoding('utf-8')
class cwdb():
    def __init__(self):
        '''初始化函数'''
        self.cwtype = 1
        self.Name = 'robojun_db_hello.db'
        self.writedata = {}
        
    def init_database_type(self,itype):
        self.cwtype = itype
        if itype == 1:#假如是糗百的数据库
            self.Name = 'D:\\warmdata\\qiubai.db'
            if os.path.exists(self.Name) == False:
                self.con =dbapi.connect(self.Name)
                self.cwdb_create(3)
            else :
                os.remove(self.Name)
                #os.unlink(my_file)
                self.con =dbapi.connect(self.Name)
                self.cwdb_create(3)
        elif itype == 2:#假如解析的是ixxzy
            self.Name = 'D:\\warmdata\\ixxzy.db'
            if os.path.exists(self.Name) == False:
                self.con =dbapi.connect(self.Name)
                self.cwdb_create(4)
            else :
                self.con =dbapi.connect(self.Name) 
        elif itype == 5:#假如解析的是知乎的数据库 
            self.Name = 'D:\\warmdata\\zhihu.db'
            if os.path.exists(self.Name) == False:
                self.con =dbapi.connect(self.Name)
                self.cwdb_create(5)
            else :
                self.con =dbapi.connect(self.Name)    
                
    def cwdb_create(self,t):
        '''创建表'''
        cur = self.con.cursor()    
        if t == 0:
            cur.execute('CREATE TABLE test2(Region TEXT,Population INTEGEN)')
        elif t == 1:
            cur.execute('CREATE TABLE PopByCountry(Region TEXT,Population INTEGEN ,Country TEXT)')
        elif t == 2:
            cur.execute('''CREATE TABLE PopByCountry(Region TEXT,Population INTEGEN ,Country TEXT)
            CONSTRAIN Country_Key PRIMARY Key (Region,Country)''')
        elif t == 3:
            cur.execute('''CREATE TABLE SPIDERDATA(ID INTEGEN,website TEXT ,contant TEXT,GoodTimes INTEGEN, siteType INTEGEN)''')
        elif t == 4:
            cur.execute('''CREATE TABLE SPIDERDATA(NAME INTEGEN,website TEXT)''')
        elif t == 5:
            cur.execute('''CREATE TABLE ANSWERDATA(Question TEXT,Answer TEXT)''')
        
        self.con.commit()
        
    def cwdb_add(self,t):
        cur = self.con.cursor()
        try:
            if t == 1:
                cur.execute('INSERT INTO PopByRegion VALUES("central africa",330993)')
                cur.execute('INSERT INTO PopByRegion VALUES("southwastern africa",743112)')
                cur.execute('INSERT INTO PopByRegion VALUES("japan",100562)')
                cur.execute('INSERT INTO PopByRegion VALUES("robojun",NULL)')
            elif t == 2:
                cur.execute('INSERT INTO PopByCountry VALUES("central africa",330993,"robocountry1")')
                cur.execute('INSERT INTO PopByCountry VALUES("southwastern africa",743112,"robocountry2")')
                cur.execute('INSERT INTO PopByCountry VALUES("japan",100562,"robocountry3")')
                cur.execute('INSERT INTO PopByCountry VALUES("robojun",NULL,"robocountry4")')
            elif t == 3:
                if len(self.writedata) >= 5:
                    cur.execute('INSERT INTO SPIDERDATA VALUES(%d,"%s","%s",%d,%d)' %(self.writedata[0],self.writedata[1],self.writedata[2],self.writedata[3],self.writedata[4]))
            elif t == 4:
                if len(self.writedata) >= 2:
                        cur.execute('INSERT INTO SPIDERDATA VALUES("%s","%s")' %(self.writedata[0],self.writedata[1]))                
            elif t == 5:
                if len(self.writedata) >= 2:
                        cur.execute('''INSERT INTO ANSWERDATA VALUES("%s","%s")''' %(self.writedata[0],self.writedata[1]))      
        except Exception as s:
            pass                    
        self.con.commit()    
        
       
    
    def cwdb_del(self,t):
        cur = self.con.cursor()
        if t == 1:
            cur.execute('DROP TABLE PopByRegion ')
        elif t == 2:
            cur.execute('DELETE FROM PopByRegion ')
        elif t == 3:
            cur.execute('DELETE FROM PopByRegion ')
        elif t == 4:
            cur.execute('DELETE FROM PopByRegion WHERE Population > 0 ')
        elif t == 5:
            cur.execute('DELETE FROM PopByRegion WHERE Population > 110000 AND Region < "L" ')
        elif t == 6:
            cur.execute('DELETE FROM PopByRegion WHERE Region = "japan"')
        print(cur.fetchall())
        print(cur.fetchone())
        self.con.commit() 
    
    
    def cwdb_find(self,t):
        cur = self.con.cursor()
        if t == 1:
            cur.execute('SELECT Region FROM PopByRegion ORDER BY Population DESC')
        elif t == 2:
            cur.execute('SELECT Population FROM PopByRegion ORDER BY Population DESC')
        elif t == 3:
            cur.execute('SELECT * FROM PopByRegion ORDER BY Population DESC')
        elif t == 4:
            cur.execute('SELECT * FROM PopByRegion WHERE Population > 110000 ORDER BY Population DESC')
        elif t == 5:
            cur.execute('SELECT * FROM PopByRegion WHERE Population > 110000 AND Region < "L" ORDER BY Population DESC')
        elif t == 6:
            cur.execute('SELECT * FROM PopByRegion WHERE Region = "japan"')
        elif t == 7:
            cur.execute('SELECT * FROM PopByCountry')
    #    elif t == 8:
    #        cur.execute('SELECT * FROM PopByCountry WHERE (SELECT * FROM PopByRegion WHERE Region = "japan") ')
        elif t == 9:
            cur.execute('SELECT * FROM SPIDERDATA')
        elif t == 10:
            cur.execute('SELECT * FROM SPIDERDATA WHERE NAME LIKE "%3%"')
        print(cur.fetchall())
        print(cur.fetchone())
        self.con.commit() 
        
    def cwdb_change(self,t):
        cur = self.con.cursor()
        if t == 0:
            cur.execute('UPDATE PopByRegion SET Population = 110 WHERE Region = "japan"')
        elif t == 1:
            cur.execute('UPDATE PopByRegion SET Population = 100562 WHERE Region = "japan"')
        
        print(cur.fetchall())        
        self.con.commit()    
        
    def cwdb_join(self):
        cur = self.con.cursor()
        cur.execute('''
        SELECT * FROM PopByRegion INNER JOIN PopByCountry
        WHERE (PopByRegion.Region = PopByCountry.Region)
        ''')
        print(cur.fetchall())
        self.con.commit()    

class qbdb(cwdb):
    def GetMaxPage(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM SPIDERDATA ORDER BY ID DESC')
        L = cur.fetchall()
        self.con.commit()    
        if len(L) == 0:
            return 0
        return int(L[0][0])
    
    def ShowTopTen(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM SPIDERDATA ORDER BY GoodTimes DESC')
        L = cur.fetchall()
        self.con.commit()  
        print("糗百 今日最佳\n\n\n")
        print("以下段子来自糗百主页_新鲜\n用爬虫爬取后按点赞排序后挑出来的\n不喜勿喷\n\n\n")
        for aword in range(20):
            text = u"作者:%s\n%s\n点赞数:%s" % (
                 L[aword][1], L[aword][2], L[aword][3])
            print("+--------华丽的分割线-----------+")
            print(text)
            print("+------------------------------+") 
        print(len(L))
        
    def Showwebsite(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM SPIDERDATA')
        L = cur.fetchall()
        self.con.commit()  
        for aword in range(len(L)):
            text = u"标题:%s\n\n网址:%s" % (
                 L[aword][0], L[aword][1])
            print("+--------华丽的分割线-----------+")
            print(text)
            print("+------------------------------+") 
        print(len(L))       
        cw.randone(len(L)-1)
    def GetRandomOne(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM SPIDERDATA')
        L = cur.fetchall()
        self.con.commit()  
        print(len(L))   
        if len(L) == 0 :
            return
        #index = cw.randone(len(L)-1)
        index = random.randint(0,len(L)-1)
        return L[index][1]
    def findFormTableixxzy(self,finded):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM SPIDERDATA WHERE NAME LIKE "%%%s%%"' %(finded))
        L = cur.fetchall()
        self.con.commit()  
        Resdata=[]
        for aword in range(len(L)):
            text = u"标题:%s\n\n网址:%s" % (
                 L[aword][0], L[aword][1])
            print("+--------华丽的分割线-----------+")
            print(text)
            Resdata.append(L[aword][0])
            Resdata.append(L[aword][1])
            print("+------------------------------+") 
        print(len(L))   
        return Resdata
    
    def GetBook(self,finded,returntype):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM ANSWERDATA WHERE Question = "%s" AND Answer LIKE "%%《%%"' %(finded))
        L = cur.fetchall()
        self.con.commit()  
        Resdata=[]
        for aword in range(len(L)):
            print(L[aword][0])
            if returntype == 1:
                str1 = L[aword][1]
                str2 = '(《.*?》)*'
                resbook = cw.find_use_re(str1,str2)
                for sinbook in resbook:
                    if len(sinbook) > 0:
                        Resdata.append(sinbook)
                        print(sinbook)
            else:
                Resdata.append(L[aword][1])
        return Resdata
       
    def Write(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM SPIDERDATA')
        L = cur.fetchall()
        self.con.commit()  
        for aword in range(len(L)):
            text = u"标题:%s\n\n网址:%s" % (
                 L[aword][0], L[aword][1])
            print("+--------华丽的分割线-----------+")
            print(text)
            print("+------------------------------+") 
        print(len(L))          
        
    def ExistInDataBase(self,newadd,databasetype):
        cur = self.con.cursor()
        if databasetype == 1:
            cur.execute('SELECT * FROM SPIDERDATA WHERE GoodTimes = "%d"' %(newadd))
        if databasetype == 2:
            cur.execute('SELECT * FROM SPIDERDATA WHERE website = "%s"' %(newadd))
        L = cur.fetchall()
        self.con.commit()    
        #print(len(L))
        if len(L) > 0:
            return True
        return False
            
        