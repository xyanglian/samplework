'''
Created on Oct 16, 2015

@author: xiaoyuyanglian
'''
def theMin(room):
    num = 0
    char=list(room)
    for i in range (len(room)-1):
        if char[i] == char [i+1]:
            char[i+1] = "Z"
            num +=1
    return num 
        
    