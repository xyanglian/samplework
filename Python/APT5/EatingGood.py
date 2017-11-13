'''
Created on Oct 8, 2015

@author: xiaoyuyanglian
'''
def howMany(meals, restaurant):
    meals = set(meals)
    res = []
    for m in meals: 
        parts = m. split(":")
        if parts [1] == restaurant and m[0] not in res:
            res.append(parts[0])
    
    return len(res)