'''
Created on Dec 2, 2015

@author: Liane Yanglian & Linda Zhou
'''
import operator

def averages(items, ratings):
    # returns a list that represents item recommendations computed by averaging item-by-item ratings
    avergs=[]
    for idx in range(len(items)):
        count=1.0
        sample=0
        for each in ratings:
            if ratings[each][idx] != 0:
                count += 1.0
                sample += ratings[each][idx]
        avergs.append((items[idx], float(sample/count)))
    print avergs
    avergs.sort(key=operator.itemgetter(0))
    avergs.sort(key=operator.itemgetter(1), reverse = True)
    return avergs

def similarities(name, ratings):
    # returns a list of per-user similarities of each user/rater to the user/rater whose name is a parameter
    slist=[]
    personrating=ratings[name]
    for k,v in ratings.items():
        if k != name:
            sim=sum([personrating[i] * v[i] for i in range(len(personrating))])
            slist.append((k,sim))
    slist.sort(key = operator.itemgetter(0))
    slist.sort(key = operator.itemgetter(1), reverse = True)
    return slist

def scores(slist,items,ratings,n):
    # returns a list of recommendations calculated for a specific user/rater by weighing user ratings more heavily for users close to the specific user
    scoreslist=[]
    for person,sim in slist[:n]:
        scoreslist.append([sim * i for i in ratings[person]])
    
    total = [0] * len(items)
    
    for sublist in scoreslist:
        total = [sublist[i]+ total[i] for i in range(len(items))]
    scores = [(items[i], total[i]) for i in range(len(items))]  
    scores.sort(key = operator.itemgetter(0))
    scores.sort(key = operator.itemgetter(1), reverse = True)
    return scores

def recommend (name, items, ratings, count):
    # returns a list of recommendations calculated for a specific user/rater
    listforrecommendations=[]
    personRatings= ratings[name]
    sList= similarities(name, ratings)
    for items in sList[:count]:
        rater = items[0]
        simi = items[1]
        rates = ratings[rater]
        averg = averages(items,ratings)
        weight = [simi * i for i in rates]
        listforrecommendations.append(personRatings,weight,averg)
        return listforrecommendations