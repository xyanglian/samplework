'''
Created on Nov 3, 2015

@author: xiaoyuyanglian
'''

def networth(transactions):
    dic = {}
    lst = []
    
    for element in transactions:
        (p,q,r) = tuple(element.split(":"))
        r = float(element.split(":")[2])
        
        if dic.has_key(p):
            dic[p] -= (r)
        else: 
            dic[p] = (r)*(-1)
       
        
        if dic.has_key(q):
            dic[q] += (r)
        else: 
            dic[q] = (r)
        
    data = sorted(dic.items())

    for var in data: 
        lst.append(str(var[0]) + ":" + str(var[1]))
    
    return lst 
    
    
    
    
        
        
    
    

    
    

