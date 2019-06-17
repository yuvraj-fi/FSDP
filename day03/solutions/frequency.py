"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""
def char_frequency(str1):
    dict1 = {}
    for n in str1:
        keys = dict1.keys()
        if n in keys:
            dict1[n] += 1
        else:
            dict1[n] = 1
    return dict1
print(char_frequency(input("enter a string")))
