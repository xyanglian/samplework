'''
Created on Sep 10, 2015

@author: xiaoyuyanglian
'''
def minutesNeeded (numCakes,capacity):
    if numCakes == 0:
        return 0 
    if numCakes <= capacity:
        return 10
    fullPansNeeded = numCakes/capacity
    t = fullPansNeeded*10
    r= numCakes % capacity
    if r > capacity/2:
        t = t + 10
    elif r != 0:
        t = t+5
    return t 

def satisfies(stuff):
    if "strengthens" in stuff:
        return 1
    if "galaxies" in stuff:
        return 4
    if "asdfasdfasdf" in stuff:
        return 3
    else:
        return 0
   