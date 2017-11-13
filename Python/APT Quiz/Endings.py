'''
Created on Dec 3, 2015

@author: xiaoyuyanglian
'''
def arrange(letter,words):
    lst = []
    for word in words:
        if word.endswith(letter):
            lst.append(word)
    return sorted(list(set(lst)))
            