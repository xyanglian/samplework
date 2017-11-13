'''
Created on Nov 24, 2015

@author: xiaoyuyanglian
'''
from operator import itemgetter
def convert(str):
    minute = int(str.split(":")[0])
    second = int(str.split(":")[1])
    return 60*minute + second

def winners(data):
    d={}
    for item in data:
        isplit = item.split()
        time = convert(isplit[1])
        if isplit[0] not in d:
            d[isplit[0]] = [0,0]
        if isplit[0] in d:
            d[isplit[0]][0]+=1
            d[isplit[0]][1]+= time
            
    org = [(g,h[0],h[1]) for g,h in d.iteritems()]
    sort = sorted(org, key = itemgetter(2), reverse = False)
    sortt = sorted(sort, key = itemgetter(1), reverse = True)
    final = [g for (g,p,q) in sortt]

    return final