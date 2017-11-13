'''
Created on Nov 16, 2015

@author: xiaoyuyanglian
'''
def bags(strength, food):
    """
      return int based on parameters strength, an int
      and food a list of Strings
    """
    count =0
    #map to find occurrences
    d={}
    for eachFood in food:
        if eachFood not in d:
            d[eachFood] =1
        else:
            d[eachFood]+=1
    for (k,v) in d.iteritems():
        if v%strength ==0:
            count+=v/strength
        else:
            count+=v/strength + 1
    return count