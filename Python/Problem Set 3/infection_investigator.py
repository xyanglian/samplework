from bwt_structures import *
from read_aligner import *
from compsci260lib import *

def reverse_complement(seq):
    """
    Returns the reverse complement of the input string.
    """
    comp_bases = {'A': 'T',
                  'C': 'G',
                  'G': 'C',
                  'T': 'A'} 
    rev_seq = list(seq)
    rev_seq = rev_seq[::-1]
    rev_seq = [comp_bases[base] for base in rev_seq] 
    return ''.join(rev_seq)
    
def align_patient_reads():
    
    """YOUR CODE GOES HERE..."""


if __name__ == '__main__':
    align_patient_reads()