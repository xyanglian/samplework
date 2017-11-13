'''
Created on Sep 18, 2015

@author: xiaoyuyanglian
'''
def coins(pence):
    a = pence / 240
    b = (pence % 240) / 12 
    c = pence - (240 *a) - (12 * b)
    return [a,b,c]

