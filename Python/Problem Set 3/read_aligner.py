from bwt_structures import *
from compsci260lib import *

def find(query, bwt_data):
    """
    Given a query sequence and a series of data structures
    containing various information about the reference genome,
    return a list containing all the locations of the query
    sequence in the reference genome. 
    """
    
    bwt, suffix_array, ranks, counts = bwt_data
      
    length = len(bwt)
    results = []
    
    """YOUR CODE GOES HERE..."""

    return sorted(results)
    
if __name__ == '__main__':
    find()