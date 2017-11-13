'''
Created on Oct 16, 2015

@author: xiaoyuyanglian
'''
def count(a,b):
    
    lstc = []
    count = 0
    lst = list(a)
    lstb = list(b)
    
    for chr in lst:
        if chr in lstb:
            lstc.append(chr)
            count += 1
            
    slstc = set(lstc)
    
    for element in slstc:
        if lst.count(element) >= lstb.count(element):
                count -= (lst.count(element)-lstb.count(element))
            
    return count 


            