import sqlite3 as dbapi

def cwdb_create(t):
    con =dbapi.connect('robojun_db_hello.db')
    cur = con.cursor()    
    if t == 0:
        cur.execute('CREATE TABLE test2(Region TEXT,Population INTEGEN)')
    elif t == 1:
        cur.execute('CREATE TABLE PopByCountry(Region TEXT,Population INTEGEN ,Country TEXT)')
    elif t == 2:
        cur.execute('''CREATE TABLE PopByCountry(Region TEXT,Population INTEGEN ,Country TEXT)
        CONSTRAIN Country_Key PRIMARY Key (Region,Country)''')
    
    con.commit()
    
def cwdb_add(t):
    con =dbapi.connect('robojun_db_hello.db')
    cur = con.cursor()
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
    con.commit()    
    
   

def cwdb_del(t):
    con =dbapi.connect('robojun_db_hello.db')
    cur = con.cursor()
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
    con.commit() 


def cwdb_find(t):
    con =dbapi.connect('robojun_db_hello.db')
    cur = con.cursor()
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
    print(cur.fetchall())
    print(cur.fetchone())
    con.commit() 
    
def cwdb_change(t):
    con =dbapi.connect('robojun_db_hello.db')
    cur = con.cursor()
    if t == 0:
        cur.execute('UPDATE PopByRegion SET Population = 110 WHERE Region = "japan"')
    elif t == 1:
        cur.execute('UPDATE PopByRegion SET Population = 100562 WHERE Region = "japan"')
    
    print(cur.fetchall())        
    con.commit()    
    
def cwdb_join():
    con =dbapi.connect('robojun_db_hello.db')
    cur = con.cursor()
    cur.execute('''
    SELECT * FROM PopByRegion INNER JOIN PopByCountry
    WHERE (PopByRegion.Region = PopByCountry.Region)
    ''')
    print(cur.fetchall())
    con.commit()
cwdb_find(8)

#con =dbapi.connect('robojun_db_hello.db')
#cur = con.cursor()

#con.commit()