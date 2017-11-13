'''
Created on Oct 22, 2015

@author: xiaoyuyanglian
'''
def encrypt(numbers):

    val = numbers.index(min(numbers))
    numbers[val] = numbers[val]+1
    
    total = 1
    for numb in numbers:
        total = total * numb
    
        
    return long(total)
    
    