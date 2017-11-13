'''
Created on Sep 18, 2015

@author: xiaoyuyanglian
'''
def bagelCount(orders):
    i = 0
    for num in orders:
        if num >= 12:
            i += num/12 + num
        else:
            i += num
    return i

