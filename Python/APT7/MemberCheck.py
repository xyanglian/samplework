'''
Created on Nov 3, 2015

@author: xiaoyuyanglian
'''
def whosDishonest(club1, club2, club3):
    lst= []
    for item in set(club1):
        if item in set(club2) or item in set(club3):
            lst.append(item) 
    for item in set(club2):
        if item in set(club1) or item in set(club3):
            lst.append(item) 
    for item in set(club3):
        if item in set(club1) or item in set(club2):
            lst.append(item) 
    return sorted(list(set(lst)))