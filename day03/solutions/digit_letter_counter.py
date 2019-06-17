"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""


st = input("Input a string")
dig=0
let=0
for c in st:
    if c.isdigit():
        dig=dig+1
    elif c.isalpha():
        let=let+1
    else:
        pass
print("Digits", dig)
print("Letter", let)
