"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
with open('absentee.txt',mode='wt')as file:
    n=0
    while n<=24:
        user_input = input("Enter values >")
        file.write(user_input + "\n")
        if not user_input:
            break
        n=n+1
with open('absentee.txt',mode='rt')as file1:
    file_contents = file1.read()
print ("absentee are",file_contents)