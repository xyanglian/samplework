'''
Created on Sep 14, 2015

@author: xiaoyuyanglian
'''

def ratio(dna):
    total = len(dna)
    a = dna.count("c")
    b = dna. count ("g")
    return (a + b)/float(total)

