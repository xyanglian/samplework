'''
@author: Liane Yanglian
@date: September 23, 2016

@note:

'''

from compsci260lib import *
import numpy


def solve_pebble():
    
    # recording all the eight possible patterns in a list of lists
    patternlist = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0],[1,0,0,1],[1,0,1,0],[0,1,0,1]]
    
    # creating a 2D array to store the eight patterns and their compatible patterns 

    pattern = numpy.zeros(shape = (8,8))
    pattern[0] = [1,1,1,1,1,1,1,1]
    pattern[1] = [1,0,1,1,1,0,1,0]
    pattern[2] = [1,1,0,1,1,1,0,1]
    pattern[3] = [1,1,1,0,1,1,1,0]
    pattern[4] = [1,1,1,1,0,0,0,1]
    pattern[5] = [1,0,1,1,0,0,0,0]
    pattern[6] = [1,1,0,1,0,0,0,1]
    pattern[7] = [1,0,1,0,1,0,1,0]
    
    # calculating the number of lines in a file 
    files = open('grid.txt')
    lines = files.readlines()
    with open('grid.txt') as file:
        numlines = sum(1 for _ in file)
    # creating another 2D array answergrid to store the results, in answergrid[i][j] is the max value that could end up at row i using pattern j 
    answergrid = numpy.zeros(shape=(numlines,8))
    #opening the file "grid.txt"
    file = open('grid.txt','rb')
    # separating the input file by lines
    data = [map(int,row.strip().split('\t')) for row in file]
    # base cases for the first row 
    answergrid[0][0] = 0
    answergrid[0][1] = data[0][3]
    answergrid[0][2] = data[0][2]
    answergrid[0][3] = data[0][1]
    answergrid[0][4] = data[0][0]
    answergrid[0][5] = data[0][0] + data[0][3]
    answergrid[0][6] = data[0][0] + data[0][2]
    answergrid[0][7] = data[0][1] + data[0][3]
    
    #for each row in the file table
    for i in range(1,numlines):
        # for each of the eight patterns in the row
        for j in range (0,len(patternlist)):
            # multiplying the max values for that pattern stored in answergrid by the compatibilities of that pattern stored in the 2D array named pattern
            compatibleoutputs = [a*b for a,b in zip(answergrid[i-1], pattern[j])]
            # getting the maximum of the outputs from the compatible patterns
            maxoutput = max(compatibleoutputs)
            # calculating the output for the single row and specific pattern in the data table 
            x = compatibleoutputs
            datalist = data[i]
            currentrowoutput = sum([a*b for a,b in zip (patternlist[j],datalist)])
            # calculating newmaxi, which is the new maximum of the sum of the current row and pattern's output and the maximum of compatible patterns' outputs for the previous row 
            newmaxi = max(compatibleoutputs) + currentrowoutput
            #updating the corresponding grid in answergrid to store the new maximum value
            answergrid[i][j] = newmaxi
            
    print 'The maximum value of a valid placement for this sample grid is',max(answergrid[numlines-1])

if __name__ == '__main__':
    solve_pebble()

