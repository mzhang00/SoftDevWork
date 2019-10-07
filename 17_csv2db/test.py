#Amanda Zheng and Michael Zhang
#SoftDev pd1
#k :: SQLITE3 BASICS
#Oct 7 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="test.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

command = "CREATE TABLE Students (name TEXT, age INTEGER, id INTEGER);" # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

with open('students.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         command = "insert into Students (name, age, id) values ('" + row['name'] + "', " + str(row['age']) + ", " + str(row['id']) + ")"
         #print(command)
         c.execute(command)    # run SQL statement
         #print(row['name'], row['age'], row['id'])

#==========================================================

db.commit() #save changes
db.close()
