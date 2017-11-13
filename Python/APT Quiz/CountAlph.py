'''
Created on Dec 3, 2015

@author: xiaoyuyanglian
'''
def summarize(words):
    """
      return int list based on strings in words
    """
    countlist =[]
    for i in range(26):
        countlist.append(0)
        
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for each in words:
        eachSplit = each.split(" ")
        eachNew = "".join(eachSplit)
        for k in range(len(eachNew)):
            lowerNew = eachNew[k].lower()
            lowerIndex = alphabets.find(lowerNew)
            if (lowerIndex!=-1):
                countlist[lowerIndex]+=1
    return countlist