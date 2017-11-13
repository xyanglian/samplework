'''
Created on Dec 3, 2015

@author: Liane Yanglian
'''

def combine(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            first = list[i]
            second = list[j]
            if len(first & second) >=2 :
                list.remove(first)
                list.remove(second)
                list.append(first|second)
                return True
    else:
        return False
                 
def edit(entry) :
    setlist =[]
    for each in entry:
        setlist.append(set(each.split(" ")))
    while combine(setlist) == True:
        pass
    final = [sorted(list((item))) for item in setlist]
    finall = [" ".join(item) for item in final]
    return sorted(finall)