"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""
user_input = input("Enter comma seperated nos >").split(",")

previous_number_is_13 = False
total = 0

for number in user_input:
    if int(number) == 13:
        previous_number_is_13 = True
    
    elif not previous_number_is_13:
        total += int(number)
    
    elif previous_number_is_13 and int(number) != 13:
        previous_number_is_13 = False

print (total)


