'''
Created on Nov 24, 2015

@author: xiaoyuyanglian
'''
def maximumFacts(suspects):
    lst=[]
    if len(suspects) ==1:
        return 0
    else:
        for num in range(len(suspects)):
            for num1 in range(num+1,len(suspects)):
                nset = set(suspects[num].split(","))
                n1set = set(suspects[num1].split(","))
                numintersect = nset & n1set
                lst.append(len(numintersect))
        return max(lst)
