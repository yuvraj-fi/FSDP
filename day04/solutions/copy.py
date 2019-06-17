"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

with open('words.txt', mode='rt') as file :
   file_contents = file.read()
with open('copy.txt',mode='wt')as file:
    file.write(file_contents)