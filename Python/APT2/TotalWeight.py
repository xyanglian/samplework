'''
Created on Sep 14, 2015

@author: xiaoyuyanglian
'''

def weight3(ab,ac,bc):
    a = (ab+ac-bc)/2
    b = (bc+ab-ac)/2
    c = (bc+ac-ab)/2
    return a + b + c
