
"""
Code Challenge
  Name: 
    Anagram
  Filename: 
    anagram.py
  Problem Statement:
   Two words are anagrams if you can rearrange the letters of one to spell the second.  
   For example, the following words are anagrams:
   ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
  
   create a function which takes two arguments and return whether they are angram or no ( True or False)
  Hint: 
   How can you tell quickly if two words are anagrams?  
   Dictionaries allow you to find a key quickly.  

"""
def anagram_chk(str1, str2):
    list1 = list(str1)
    list1.sort()
    list2 = list(str2)
    list2.sort()

    return (list1 == list2)

print(anagram_chk('tabes','beast'))
