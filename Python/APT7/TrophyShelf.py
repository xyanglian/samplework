'''
Created on Nov 3, 2015

@author: xiaoyuyanglian
'''
def countVisible(trophies):
    leftmax = trophies[0]
    new = [i for i in reversed(trophies)]
    rightmax = new[0]
    left = 1
    right = 1
    for index in range(1,len(trophies)):
        if trophies[index] > leftmax:
            left += 1
            leftmax = trophies[index]
    for index in range(1, len(trophies)):
        if new[index] > rightmax:
            right += 1
            rightmax = new[index]
    return [left,right]