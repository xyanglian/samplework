'''
Created on Oct 22, 2015

@author: xiaoyuyanglian
'''

def getMaximumSubset(words):
    for i in range(0,len(words)):
        new = sorted(words[i])
        words[i] ="".join(new)
        #New = "".join(new)
    return len(set(words))


        
