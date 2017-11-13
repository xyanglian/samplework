'''
@author: Liane Yanglian
@date: September 12, 2016

@note: 

'''

import sys
from compsci260lib import *
from orfs import *


def solve_ssRNA(RNAsequence):
    # combining many small overlapping reads into a longer sequenec of bases

    list2 = []
    # appending all the reads into a list
    for b in range(0,20):
        list2.append(RNAsequence[b]) 
    #making a dictionary with the first twenty nucleotides as the key and the rest of the nucleotides as the values for each read
    sequences = {q[:20]:q[20:] for q in list2}
    #making a set of the last twenty nucleotides of each read
    lastchars = set(q[-20:] for q in list2)
    #searching through the keys of the sequences library, taking the first sequence's first twenty characters as the first value
    firstchars = next(v for v in sequences if v not in lastchars)
    #initializing newsequence
    newsequence = [firstchars]
    # while the firstchars corresponds to some read's first twenty characters
    while firstchars in sequences:
        #appending the value of that firstchars in the sequences dictionary
        newsequence.append(sequences[firstchars])
        # updating firstchars to the last twenty nucleotides of the same read
        firstchars = sequences[firstchars][-20:]
    answer = ''.join(newsequence)
    print 'The number of nucleotides in the RNA sequence I assemble is', len(answer)
    return answer

if __name__ == '__main__':
    
    RNAsequence = get_fasta_dict('ssRNA.fasta').values()
    
    sequence = solve_ssRNA(RNAsequence).upper()

    for n in [70]:
        solve_orfs(sequence,n)
        
        