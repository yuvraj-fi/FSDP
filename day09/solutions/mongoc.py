"""Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database."""

import pymongo

client = pymongo.MongoClient("mongodb://yuvraj:qwer@cluster0-shard-00-00-9vevf.mongodb.net:27017,cluster0-shard-00-01-9vevf.mongodb.net:27017,cluster0-shard-00-02-9vevf.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

mydb = client.db_University

def add_employee(student_name,student_age,student_roll_no,studdent_branch ):
   
    mydb.student.insert_one(
            {
            "student_name" : student_name,
            "student_age" : student_age,
            "student_roll_no" : student_roll_no,
            "studdent_branch" : studdent_branch
            })
    return "student added successfully"


def fetch_all_student():
    user = mydb.student.find()
    for i in user:
        print (i)




add_employee('Kovid',21,18,'cs')
add_employee('rahul',21,19,'cs')
add_employee('mahesh',22,17,'cs')
add_employee('Yuvraj',20,21,'cs')
add_employee('mayank',21,4,'cs')

fetch_all_student()