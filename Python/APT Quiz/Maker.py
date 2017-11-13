'''
Created on Nov 3, 2015

@author: xiaoyuyanglian
'''
def canMake(message, letterlist):
    new = list("".join(letterlist))
    for letter in message:
        if letter.lower() not in new:
            return "no"
    return "yes"
            