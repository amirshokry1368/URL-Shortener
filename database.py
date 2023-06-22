import sqlite3

def addUser(name,email,password):
    conn=sqlite3.connect('Links.db')
    cursor=conn.cursor()
    cursor.execute(
        'insert into Users(name,email,password) values(?,?,?)',
        (name,email,password)
    )
    conn.commit()
    conn.close()

def validUser(email,password):
    conn=sqlite3.connect('Links.db')
    cursor=conn.cursor()
    cursor.execute(
        'select email,password from Users where email=? and password=?',
        (email,password)
    )
    result=cursor.fetchall()
    conn.close()
    if(len(result)>0):
        return True
    else:
        return False


def addLink(longL,shortL):
    conn=sqlite3.connect('Links.db')
    cursor=conn.cursor()
    cursor.execute(
        'insert into links(long,short) values(?,?)',
        (longL,shortL)
    )
    conn.commit()
    conn.close()
    

def getLongLink(short):
    conn=sqlite3.connect('Links.db')
    cursor=conn.cursor()
    cursor.execute(
        'select long from links where short=?',
        (short,)
    )
    result=cursor.fetchone()[0]
    conn.close()
    return result