#Amanda Zheng and Michael Zhang
#SoftDev pd1
#k :: SQLITE3 BASICS
#Oct 7 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="test.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

with open('students.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['name'], row['age'],row['id'])

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()
