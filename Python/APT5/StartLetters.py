'''
Created on Oct 16, 2015

@author: xiaoyuyanglian
'''

def howManyLetters(phrase):
    lst = []
    num = 0 
    words = phrase.split()
    for i in range(len(words)):
        wordslower = words[i][0].lower()
        lst.append(wordslower)
        
    if lst != []:
        st = set(lst)
    else: 
        num = 0
        return num

    for i in range(len(st)):
        num += 1
    return num 

