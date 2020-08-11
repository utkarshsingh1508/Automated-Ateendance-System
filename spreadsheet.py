from openpyxl import Workbook, load_workbook
import time
import os
import sqlite3


#database connection
conn = sqlite3.connect('Face-DataBase3')
c = conn.cursor()

#get current date
currentDate = time.strftime("%d/%m/%y")
currentTime = time.strftime("%H:%M:%S")

currentDate2 = time.strftime("%d_%m_%y")
currentTime2 = time.strftime("%H_%M")

name=input("Enter your name")
path=os.getcwd()
st=str(path+"\\reports\\"+name+"_"+currentDate2)
#create a workbook and add a worksheet
if not(os.path.exists(st)):
    os.makedirs(st)
    
wb = Workbook()
dest_filename = st+"\\"+name+"_"+currentTime2+'.xlsx'
c.execute("SELECT * FROM Students ORDER BY Roll ASC")

#creating worksheet and giving names to column
ws1 = wb.active
ws1.title = "Attendance Sheet"
ws1.append(('Roll Number', 'Name', 'Date','Time'))


#entering students information from database
while True:
    a = c.fetchone()
    if a == None:
        break
    else:
        ws1.append((a[2], a[1],currentDate,currentTime))

#saving the file
wb.save(filename = dest_filename)
