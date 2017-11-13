'''
Created on Nov 16, 2015

@author: xiaoyuyanglian
'''
def compare(deeds, needString):
    # a boolean helper method to compare whether each need in needString is in deeds
    needSplit = needString.split(" ")
    for eachNeed in needSplit:
        if eachNeed not in deeds:
            return False
    return True
    
def findLabel(labels,deeds,needs):
    for i in range(len(labels)):
        current = labels[i]
        if compare(deeds,needs[i])==True:
            return current
    return "nobadge"