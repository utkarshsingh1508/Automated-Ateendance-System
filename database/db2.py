import sqlite3
def createTable():
    connection=sqlite3.connect("Face-DataBase3")
    connection.execute("CREATE TABLE Students(ID INT PRIMARY KEY NOT NULL,Name TEXT NOT NULL ,Roll TEXT,Presents INT,LastUpdatedTime datetime)")
    connection.commit()
    connection.close()
createTable()    
