'''
@author: Liane Yanglian
@date: September 12, 2016

@note:

'''


import sys, random
from compsci260lib import *

def solve_orfs(sequence, n):
    """Your code goes here..."""
    listoforfs = []
    orfdict = {}

    for i in range (0,3):
        seq = sequence [i:]
        for j in range (i,len(seq),3):
            startcodon = seq[j:j+3]
            endindex= -1
            if "AUG" == startcodon:
               if j > endindex:
                    orfdict ['start'] = j
                    endindex = j
                    for k in range(j,len(seq),3):
                        stopcodon = seq[k:k+3]
                        if "UAG" == stopcodon or "UGA" == stopcodon or "UAA" == stopcodon:
                            if k-endindex >= n:
                                orfdict ['stop'] = k-1
                                orfdict ['frame'] = i
                                orfdict ['stopcodon'] = stopcodon
                                orfdict['nnlength'] = k-endindex
                                orfdict ['aalength'] = (k-endindex) / 3
                                orfdict ['strand'] = "+"
                                listoforfs.append(orfdict)
    print len(listoforfs)
    return listoforfs

def random_amino_acid (aacid): 
    list = ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
    n = random.randint[0,21]
    if n != aacid:
        accid = list[n]
        
    
def random_nucleotide (nucleotide):    
    list = ["A","C","G","T"]
    n =  random.randint[0,5]
    if n != nucleotide:
        nucleotide = list[n]
    
    
        
                   
               
               
            
    

















if __name__ == '__main__':
    sequence = get_fasta_dict('sars.fasta').values()[0]
    for n in [70]:
        solve_orfs(sequence,n)
    