"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
def fix_teen(n):
    if n in range(13,20):
        if n == 15 or n== 16:
            return n
        else:
            return 0
    else:
        return n
    
str1= input("enter a dictionary")
Sum=0
import ast
dict1 = ast.literal_eval(str1)
for value in dict1.values():
    Sum=Sum+fix_teen(value)
print(Sum)