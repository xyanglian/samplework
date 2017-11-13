'''
Created on Sep 14, 2015

@author: xiaoyuyanglian
'''
def shorten(name):
    list = name.split()
    if len(list) > 1:
        return list[0] + " " + list[-1]
    return name 
    
def satisfies(stuff):
    list = stuff.split(",")
    if len(list) > 7:
        return stuff.count(list)
    else:
        return 0