'''
Created on Oct 22, 2015

@author: xiaoyuyanglian
'''

def points(player, dictionary):
    score = 0 
    for word in set(player):
        if word in dictionary:
            score += len(word)**2
    return score 