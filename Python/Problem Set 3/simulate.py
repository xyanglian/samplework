import sys, random
from compsci260lib import *
from math import exp
import numpy

def simulate():
     
    G = 3000000;
    R = 45000;
    L = 500;
    iterations = 20;
    notcovered = 0
    # repeating the sequencing process iterations times 
    for k in range(0,iterations):
        # setting all G elements in the list to 0 
        genome = [0]*G
        # randomly selecting starting locations for R reads 
        for i in range(0,R):
            # the bounds are 0 to G-L because the length of each read is L in length
            randomnumber = random.randint(0,G-L)
            # updating the number of times the nucleotides covered by the read were sequenced 
            for j in range(randomnumber,randomnumber+L):
                genome[j] = genome[j] + 1
    coverage = float(float(sum(genome))/float(G))
    for l in range(0,G):
        if genome [l] == 0:
            notcovered +=1 
            
                 
if __name__ == '__main__':
    simulate()
