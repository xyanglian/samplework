'''
Version 2 on November 1, 2015

Original: Oct 24, 2012

@author: Liane Yanglian and Linda Zhou 
'''

import csv

def readandprocess(name):
    csvf = open(name,'rb')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    datad = {}
    header = freader.next()
    for row in freader:
        artist = row[2]
        song=row[1]
        if artist not in datad:
            datad[artist]=[song]
        else:
            datad[artist].append(song)
    info = datad.items() 
    tosort = [(len(t[1]),t[0]) for t in info] 
    info = sorted(tosort) 
    wordss={}
    for songs in datad.values():
        for title in songs:
            words=title.split()
            for w in words:
                if len(w)>3:
                    if w not in wordss:
                        wordss[w]=1
                    else:
                        wordss[w]+=1
    wordsss=wordss.items()
    sortwords=[(v,k) for (k,v) in wordsss]
    print sorted(sortwords)[-1]
                


if __name__ == '__main__':
    readandprocess("top1000.csv")