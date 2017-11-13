'''
@author: Liane Yanglian
@date: September 11, 2016

@note: 

'''

import sys
import re
from compsci260lib import *
newlist = []

def solve_p53():
    
    """Your code goes here..."""
    dict = get_fasta_dict("p53.fasta")
    stringdict = str(dict.values())
    startofcoding = 11716;
    endofcoding = 18676;
    codingplusintrons = stringdict [ startofcoding : endofcoding + 1]
    concantenating = codingplusintrons +  stringdict [18677:18680] 

 
    if (re.match (r'^ATG', concantenating)) and ( ( re.match (r'^TAA', concantenating [::-1])) or ( re.match (r'^TAG', concantenating [::-1])) or ( re.match (r'^TGA', concantenating [::-1] ))):
        print yes;
 
    if re.search("CACGTG",codingplusintrons):
        print "CACGTG at" , re.search("CACGTG",codingplusintrons).start()
     
    if re.search("CGCCGGCG",codingplusintrons):
       print "CGCCGGCG at" , re.search("CGCCGGCG",codingplusintrons).start()
             
    if re.search("CACCGGCG",codingplusintrons):
        print "CACCGGCG at" , re.search("CACCGGCG",codingplusintrons).start()
         
    if re.search("CACCGGTG",codingplusintrons):
        print "CACCGGTG at" ,re.search("CACCGGTG",codingplusintrons).start()
             
    if re.search("CGCCGGTG",codingplusintrons):
        print "CGCCGGTG at" ,re.search("CGCCGGTG",codingplusintrons).start()
             
    if re.search("CAC",codingplusintrons) and re.search("GTG", codingplusintrons [codingplusintrons.index("CAC")+7]):
        for n in range (1,5):
            newlist [n-1] == codingplusintrons [re.search("CAC",codingplusintrons).end() + n]
            stringlist = ''.join(newlist)
        print "CAC" + stringlist + "GTG"
     
    return stringdict








if __name__ == '__main__':
#     solve_p53()
    stringdict = solve_p53()
    print stringdict [17519:17522]

