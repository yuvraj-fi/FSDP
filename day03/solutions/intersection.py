"""Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""

list1=[1,3,6,78,35,55]
s1=set(list1)
list2=[12,24,35,24,88,120,155]
s2=set(list2)
list3=list(s1.intersection(s2) )
print(list3)