'''
Created on Oct 29, 2015

@author: xiaoyuyanglian
'''
import SimpleCaesar
from encore.storage.tests.static_url_store_test import count

def loadWords(filename):

    allwords = []
    f = open(filename)
    for line in f:
        line = line.strip()
        allwords.append(line)
    f.close()
    return allwords

def makeSet():
    count = 0
    collection = set(allwords)
    for element in collection: 
        for shift in range(1,26):
            x = SimpleCaesar.encrypt(element, shift)
            if x in collection:
                count += 1
            else:
                count = count
    print count 
    
if __name__ == '__main__': 
    allwords = loadWords("lowerwords.txt")
    makeSet()
    