'''
Created on Nov 3, 2015

@author: xiaoyuyanglian
'''
def nameDonor(contributions):
    d=dict()
    total = []
    
    for i in contributions:
        i = i.split(":")
        if i[0] not in d.keys():
            d[i[0]] = 0
        d[i[0]] += float(i[1])
            
    maxV = 0
    maxN = []
    for key in d.keys():
        if (d[key]) == maxV:
            maxN.append(key)
        if (d[key])>maxV:
            maxV = (d[key])
            maxN= [key] 
    return sorted(maxN)[0]

    