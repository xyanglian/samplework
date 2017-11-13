'''
Created on Nov 3, 2015

@author: xiaoyuyanglian
'''
#if my value is bigger than the max, that's when I stop stealing 


def minimumVotes(votes):
    newV = votes[1:]
    count = 0
    
    if votes[0] == max(votes) and votes.count(max(votes)) == 1:
        return count
    
    if len(votes) <= 1:
        return count 
    
    while votes[0] <= max(newV) or votes.count(max(votes)) > 1:
        newV[newV.index(max(newV))] -= 1
        votes [0] += 1
        count += 1 
        if votes[0] > max(newV):
            break 
        
    return count
# newV votes [1: ]
#if first item is the maximum and the only one, then return count
#if there's only one item in votes, return count
# while votes[0] <= max, or if num of max votes more than 1, subtract, add, and then update count, if votes > max (newV), breal
