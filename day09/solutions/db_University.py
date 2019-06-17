"""

Code Challenge 1
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""

import sqlite3
#from pandas import DataFrame
 
conn = sqlite3.connect ( 'db_University.db' )

c = conn.cursor()
c.execute("drop table student")

c.execute ("""CREATE TABLE student(
          Student_name TEXT,
          Student_age INTEGER,
          Student_roll_no INTEGER,
          Student_Branch TEXT
          )""")
c.execute("INSERT INTO student VALUES ('Kovid',21,18,'cs')")
c.execute("INSERT INTO student VALUES ('rahul',21,19,'cs')") 
c.execute("INSERT INTO student VALUES ('mahesh',22,17,'cs')")
c.execute("INSERT INTO student VALUES ('Yuvraj',20,21,'cs')")
c.execute("INSERT INTO student VALUES ('mayank',21,4,'cs')")

c.execute("SELECT * FROM student")
print ( c.fetchall() )

conn.commit()

conn.close()