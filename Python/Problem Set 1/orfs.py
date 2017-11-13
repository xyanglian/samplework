'''
@author: Liane Yanglian
@date: September 12, 2016

@note:

'''


import sys, random
from compsci260lib import *

def random_amino_acid (aacid): 
    # taking an amino acid as input and randomly changing it into another amino acid by mutation 
    list = ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
    n = list[random.randint(0,19)]
    while n == aacid:
    
       n = list[random.randint(0,19)]
       
    if n != aacid:
           accid = n
    return n

def random_nucleotide (nucleotide):    
    # taking a nucleotide as input and randomly changing it into another nucleotide 
    list = ["A","U","G","C"]
    n =  list[random.randint(0,3)]
    
    while n == nucleotide:
        n = list [random.randint(0,3)]
        
    if n != nucleotide:
        nucleotide = n
    return n
def solve_orfs(sequence, n):
    #taking as input a genome sequence and the minimum length of an ORF in amino acids and returning a list of dictionaries, each entry of the list corresponding to one ORF, and each dictionary containing entries providing information about that ORF
    lengthlist = []
    startlist = []
    stoplist = []
    # taking as input a genome sequence and the minimum length of an ORF in amino acids, and returning a list of dictionaries
    listoforfs = []
    sum = 0
    listofthirdorf = []

    # having i represent the reading frame with respect to the start of the genome 
    for i in range (0,3):
        orfdict = {}
        seq = sequence [i:]
        startcodonindex= -1
        # looking at the sequence, three nucleotides at a time for a start codon 
        for j in range (i,len(seq)-4,3):
            startcodon = seq[j:j+3]
            if "AUG" == startcodon and j > startcodonindex:
                # adding i to the start codon value so that the location can be referred to regardless of its reading frame
                orfdict ['start'] = j + i
                startlist.append(orfdict ['start'])
                 # looking at the sequence, three nucleotides at a time for a stop codon 
                for k in range(j+3,len(seq)-4,3):
                    stopcodon = seq[k:k+3]
                    if stopcodon == "UAG" or stopcodon == "UGA" or stopcodon == "UAA" :
                    # checking if the length of the sequence is bigger than or equal to the minimum ORF length in nucleotides
                        if k - j >= n*3:
                            orfdict ['stop'] = k-1 +i
                            stoplist.append(orfdict ['stop'])
                            orfdict ['frame'] = i
                            orfdict ['stopcodon'] = stopcodon
                            orfdict['nnlength'] = k-j
                            orfdict ['aalength'] = (k-j) / 3
                            sum += orfdict ['aalength']
                            orfdict ['strand'] = "+"
                            orfdict['length'] = (k-1-j) 
                            lengthlist.append(orfdict['length'])
                            listoforfs.append(orfdict)
                            startcodonindex = k
                            orfdict = {}
                        break
                    
    #(for problem 3) getting the largest sequence from the list of ORFs and translating it 
    largetssequence = sequence[ listoforfs[lengthlist.index(max(lengthlist))]['start']: listoforfs[lengthlist.index(max(lengthlist))]['stop']]
    translatedlargest = translate(largetssequence)
    print '(only for Problem 3), largest ORF  is',translatedlargest
    for g in range(0,len(listoforfs)):
        print '(only for Problem 3) The length of the ORF is',listoforfs [g] ['length'] 
    # (for problem 3), computing the fraction of the genome that is coding 
    frictioncoding = float((max(stoplist)-min(startlist)))/float(len(sequence))
    print '(only for Problem 3), the friction of the genome that is coding is,' , frictioncoding
    # printing the average amino acid length
    print "(only for Problem 2), average amino acid length is" , sum/len(listoforfs)
    # when the minimum ORF length is 40 amino acids 
    if n == 40:
        # sorting the list of ORFs by its start values
        sortedorfs = sorted(listoforfs, key=lambda s: s['start']) 
        # finding the third ORF in the 5' to 3' direction
        thethirdorfsequence = seq[sortedorfs[2]['start']:sortedorfs[2]['stop']]
        # translating the third ORF sequence 
        translated = translate(thethirdorfsequence)
        # translating the initial ORF sequence into the corresponding protein
        mutate_amino_acid(translated)
        mutate_nucleotide(thethirdorfsequence)
    print "The number of ORFS the procedure finds is:",len(listoforfs)
    print 'The list of ORFs is', listoforfs
    return listoforfs

def mutate_nucleotide (nucleotide_sequence):
    # selecting a random position in the sequence and applying the random_nucleotide mutation function to that position 
    for i in range (0,21):
        mutationplace = random.randint(0,len(nucleotide_sequence)-1)
        nucleotide_sequence = nucleotide_sequence [:mutationplace] + random_nucleotide(nucleotide_sequence [mutationplace]) + nucleotide_sequence[mutationplace+1:]
        newnucsequence = translate(nucleotide_sequence)
        print 'protein sequences with changed nucleotides',newnucsequence
 
  
  
def mutate_amino_acid (aminoacid_sequence):
    # repeatedly selecting random positions in the protein sequence (obtained from translating the initial ORF sequence into the corresponding protein) and applying the random_amino_acid mutation function 
    for i in range (0,21):
        mutationplace = random.randint(0,len(aminoacid_sequence)-1)
        aminoacid_sequence =  aminoacid_sequence [:mutationplace] + random_amino_acid (aminoacid_sequence[mutationplace]) + aminoacid_sequence [mutationplace+1:]
        print 'protein sequences with changed amino acids',aminoacid_sequence

if __name__ == '__main__':
    #applying the procedure to the SARS genome
    sequence = get_fasta_dict('sars.fasta').values()[0]
    # finding out the number of ORFs the procedure finds when the minimum ORF length is 10, 40, or 70 amino acids
    for n in [10, 40, 70]:
        solve_orfs(sequence,n)
        




