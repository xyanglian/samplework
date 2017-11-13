'''
Created on Sep 10, 2015

@author: xiaoyuyanglian
'''

def is_vowel(ch):
    if ch == "e":
        return True
    if ch == "E":
        return True
    if ch == "a":
        return True
    if ch == "A":
        return True
    if ch == "i":
        return True
    if ch == "I":
        return True
    if ch == "o":
        return True
    if ch == "O":
        return True
    if ch == "u":
        return True
    if ch == "U":
        return True
    return False

def repeat(word,number):
    if is_vowel (word[0]):
        return word
    if len(word) > 2 and is_vowel (word[2]):
        first = word [0:3]
        firstLower = first.lower()
        ret = first + (firstLower * (number-1))
        return ret + word[3:]
    if len(word) > 1 and is_vowel(word[1]):
        first = word [0:2]
        firstLower=first.lower()
        ret = first + (firstLower * (number-1))
        return ret + word[2:]
    return word 

    
        