'''
Created on Oct 22, 2015

@author: xiaoyuyanglian
'''
def score(listA,listB,listC):
    scoreA = 0
    scoreB = 0
    scoreC = 0
    for word in listA:
        if word not in listB and word not in listC:
            scoreA += 3
        if word not in listB and word in listC:
            scoreA += 2
        if word not in listC and word in listB:
            scoreA += 2
        if word in listB and word in listC:
            scoreA += 1
    
    for word in listB:
        if word not in listA and word not in listC:
            scoreB += 3
        if word not in listA and word in listC:
            scoreB += 2
        if word not in listC and word in listA:
            scoreB += 2
        if word in listA and word in listC:
            scoreB += 1
            
    for word in listC:
        if word not in listA and word not in listB:
            scoreC += 3
        if word not in listA and word in listB:
            scoreC += 2
        if word not in listB and word in listA:
            scoreC += 2
        if word in listA and word in listB:
            scoreC += 1
            
    return str(scoreA)+"/"+str(scoreB)+"/"+str(scoreC)