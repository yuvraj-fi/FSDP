"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and in membership Operator
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'Clfrn', 'klhm', 'Flrd']
    
"""


  
 
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida'] 
vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')  
for x in state_name:
    y=x
    for a in y :
        if a in vowels:
            y=y.replace(a,"")
    print(y)  