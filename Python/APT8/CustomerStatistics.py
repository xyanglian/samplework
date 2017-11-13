'''
Created on Nov 10, 2015

@author: xiaoyuyanglian
'''
def reportDuplicates(names):
    namelist = []
    lst = []
    for name in names:
        if name not in namelist:
            namelist.append(name)
    for name in sorted(namelist):
        if names.count(name) > 1:
            lst.append(name+" "+str(names.count(name)))
    return lst 