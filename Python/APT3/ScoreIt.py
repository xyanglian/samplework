'''
Created on Sep 18, 2015

@author: xiaoyuyanglian
'''

def maxPoints(toss) :
    numberlist = [0,0,0,0,0,0]
    for num in toss:
        numberlist[num-1] += num 
    i = 0
    for num in numberlist:
        if num > i:
            i = num
    return i