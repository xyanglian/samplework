'''
Created on Dec 4, 2015

@author: xiaoyuyanglian
'''
def highestScore(friends):
    lst =[]
    for item in friends:
        lst.append([]) 

    for k in range(len(friends)):
        for i in range(len(friends)):
            if friends[k][i] == "Y":
                lst[k].append(i)
                for j in range(len(friends)):
                    if friends[i][j] == "Y" and friends[k][j] =="N" and j!=k:
                        if j not in lst[k]:
                            lst[k].append(j)

    listofcount =[]
    for list in lst:
        listofcount.append(len(list))
    return max(listofcount)