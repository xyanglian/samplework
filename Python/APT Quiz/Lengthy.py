'''
Created on Dec 3, 2015

@author: xiaoyuyanglian
'''
from operator import itemgetter

def sizings(words):
    """
    return list sorted by length
      """

    d={}
    answer=[]
    final=[]
    setter = set(words)
    sets = list(setter)
    for i in range(len(sets)):
        if sets[i] not in d:
            d[sets[i]] = len(sets[i])
  
    for (k,v) in d.iteritems():
        answer.append([k,v])
    
    answer1 = sorted(answer, key = itemgetter(0))
    answer2 = sorted(answer1, key = itemgetter(1))
    for (k,v) in answer2:
        final.append(k)
    return final
