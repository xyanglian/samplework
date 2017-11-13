'''
Created on Nov 3, 2015

@author: xiaoyuyanglian
'''
def clubsize(names, club):
    count = 0
    for element in set(names):
        if element in set(club):
            count +=1
    return count 

    
    