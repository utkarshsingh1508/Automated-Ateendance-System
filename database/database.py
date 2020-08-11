import sqlite3
def createTable():
    connection=sqlite3.connect("login.db")
    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,EMAIL TEXT ,PASSWORD TEXT)")
    connection.execute("INSERT INTO USERS VALUES(?,?,?)",('admin123','utkarsh123','utkarsh'))
    connection.commit()
    connection.close()
createTable()    
