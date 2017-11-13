'''
Created on Sep 29, 2015

@author: xiaoyuyanglian
'''
import math 
from math import sqrt

def is_prime(num):
    if num == 1:
        return False
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            return False 
    return True
def pcount(low,high):
    count = 0
    for num in range(low,high):
        if is_prime(num):
            count += 1 
    return count
    
    
    
        
    