'''
Created on Oct 16, 2015

@author: xiaoyuyanglian
'''

def namesForYear(courses, year):
    courseyr = []
    lst = []
    for x in courses:
        x = x.split(":")
        for y in range(2,len(x),2):
            courseyr += [x[y]]
            if year not in list(set(courseyr)):
                newn = "" 
            else:
                if x[y] == year:
                    lst += [x[y-1]]
                    name = " ".join(list(set(lst))).split()
                    newn = " ".join(sorted(name))
    return newn
