'''
@author: Liane Yanglian
@date: September 11, 2016

@note: 

'''

import sys
import re
from compsci260lib import *

def solve_p53():
    
    dict = get_fasta_dict("p53.fasta")
    stringdict = str(dict.values()[0])
    #storing the locations of the beginning and end of the coding region in startofcoding and endofcoding 
    startofcoding = 11716;
    endofcoding = 18676;
    #extracting the part of the sequence between the beginning and the end of the coding region 
    codingplusintrons = stringdict [ startofcoding : endofcoding + 1]
    #concatenating the coding plus introns sequence with the next three nucleotides 
    concantenating = codingplusintrons +  stringdict [18677:18680] 
    #validating the new sequence starts with an ATG codon and ends with a stop codon
    if re.match (r'^ATG', concantenating) and  re.match (r'^(TAG)|(TGA)|(TAA)', concantenating [-3:]) :
        print "Yes, the sequence starts with an ATG and ends with a stop codon!";
    #checking if the coding plus intron sequence contains a restriction site for PmII and reports it and its location if it does
    if re.search("(?=CACGTG)",codingplusintrons):
        print "for PMII, CACGTG at" , re.search("CACGTG",codingplusintrons).start()
    #checking if the coding plus intron sequence contains a restriction site for SgrAI and reports it and its location if it does
    if re.search(r"C[G|A]CCGG[C|T]",codingplusintrons):
        print "for SgrAI,", codingplusintrons[re.search(r"C[G|A]CCGG[C|T]",codingplusintrons).start():re.search(r"C[G|A]CCGG[C|T]",codingplusintrons).start()+8], "at", re.search(r"C[G|A]CCGG[C|T]",codingplusintrons).start()
    #checking if the coding plus intron sequence contains a restriction site for Olil and reports it and its location if it does
    if re.search("CAC....GTG",codingplusintrons):
            print "for OliI, CAC" + codingplusintrons [(re.search("CAC....GTG",codingplusintrons).start()+3):(re.search("CAC....GTG",codingplusintrons).start()+7)] + 'GTG at' ,re.search("CAC....GTG",codingplusintrons).start()
    return stringdict








if __name__ == '__main__':
    stringdict = solve_p53()
    # printing the nucleotides from 17520 to 17522
    print "The nucleotides from 17520 to 17522 are",stringdict [17519:17522],"."

