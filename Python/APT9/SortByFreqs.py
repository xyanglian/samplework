'''
Created on Nov 24, 2015

@author: xiaoyuyanglian
'''
from operator import itemgetter
def sort(data):
    d = {}
    for word in data:
        if word not in d:
            d[word] = 0
        d[word] += 1
    item = d.items()
    item.sort()
    item.sort(key=itemgetter(1),reverse = True)
    return [word[0] for word in item]
