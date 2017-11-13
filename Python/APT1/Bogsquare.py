'''
Created on Sep 7, 2015

@author: xiaoyuyanglian
'''
def sumTo(aBound):
    theSum = 0
    for aNumber in range(1, aBound+1):
        theSum = theSum + aNumber

    return theSum

print(sumTo(4))

print(sumTo(1000))
