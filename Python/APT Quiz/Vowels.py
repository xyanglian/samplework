'''
Created on Sep 21, 2015

@author: xiaoyuyanglian
'''
def weight(word):
    a = word.count("a")
    b = word.count("e")
    c = word.count ("i")
    d = word.count ("o")
    e = word.count ("u")
    f = word.count ("A")
    g = word.count ("E")
    h = word.count ("I")
    i = word.count ("O")
    j = word.count ("U")
    return float(a+b+c+d+e+f+g+h+i+j) / len(word)
