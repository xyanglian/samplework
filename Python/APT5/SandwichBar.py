'''
Created on Oct 16, 2015

@author: xiaoyuyanglian
'''

def whichOrder(available, orders):
        for x in range(len(orders)):
            newx = orders[x].split()
            i = 0
            for y in newx:
                if y not in available:
                    i = i + 1
            if i == 0:
                return x
        if i!= 0:
            return -1
        
 
 

