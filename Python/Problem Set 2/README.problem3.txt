Course: COMPSCI 260
Name: Liane Yanglian
NetID:xy48
Problem: 3
Problem Set: 2
Due: Fri 30 Sep 2016, 5pm
Using free extension (yes/no): no

Statement of collaboration and resources used (put None if you worked 
entirely without collaboration or resources; otherwise cite carefully):
I consulted these and borrowed ideas from these resources:TA Lydia Xu, TA Jack Michuda, TA Shariq Iqbal, 
http://stackoverflow.com/questions/19001402/how-to-count-the-total-number-of-lines-in-a-text-file-using-python
http://stackoverflow.com/questions/10937918/loading-a-file-into-a-numpy-array-with-python and http://stackoverflow.com/questions/11354544/read-lines-containing-integers-from-a-file-in-python
My solutions and comments for this problem are below.
-----------------------------------------------------
a) There are 8 distinct valid pebble placements that can occur in a single row. They are as follows (if nothing is placed on a grid, then
I note it as 0; otherwise, I note is 1)

Pattern 0: 0,0,0,0
Pattern 1: 0,0,0,1
Pattern 2: 0,0,1,0
Pattern 3: 0,1,0,0
Pattern 4: 1,0,0,0
Pattern 5  1,0,0,1
Pattern 6: 1,0,1,0
Pattern 7: 0,1,0,1

b) The algorithm I designed is as follows (for specifc comments, please refer to the code in the .py file):
pseudo code with English explanation: 

First, create a list of lists named patternlist to store the aforementioned 8 patterns. 
patternlist = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0],[1,0,0,1],[1,0,1,0],[0,1,0,1]]

create 2D array to store the eight patterns and their compatible patterns
pattern[0] = [1,1,1,1,1,1,1,1]
pattern[1] = [1,0,1,1,1,0,1,0]
pattern[2] = [1,1,0,1,1,1,0,1]
pattern[3] = [1,1,1,0,1,1,1,0]
pattern[4] = [1,1,1,1,0,0,0,1]
pattern[5] = [1,0,1,1,0,0,0,0]
pattern[6] = [1,1,0,1,0,0,0,1]
pattern[7] = [1,0,1,0,1,0,1,0]

files = open('grid.txt')
    lines = files.readlines()
    with open('grid.txt') as file:
        numlines = sum(1 for _ in file)
        
Then, create another 2D array answergrid to store the results, in answergrid[i][j] is the max value that could end up at row i 
using pattern j. Then give the base cases for answergrid.
Then separate the input file by line.
    file = open('grid.txt','rb')
    data = [map(int,row.strip().split('\t')) for row in file]
 answergrid[0][0] = 0
 answergrid[0][1] = data[0][3]
 answergrid[0][2] = data[0][2]
 answergrid[0][3] = data[0][1]
 answergrid[0][4] = data[0][0]
 answergrid[0][5] = data[0][0] + data[0][3]
 answergrid[0][6] = data[0][0] + data[0][2]
 answergrid[0][7] = data[0][1] + data[0][3]

for each row in the input file table:
	for each of the eight patterns:
		multiply the max values for that pattern stored in answergrid by the compatibilities of that pattern stored in the 2D array named
		pattern
		compatibleoutputs = [a*b for a,b in zip(answergrid[i-1], pattern[j])]
		store the maximum of the outputs from the compatible patterns in a variable
		calculate the output for the single row and specific pattern in the data table 
        x = compatibleoutputs
        datalist = data[i]
        currentrowoutput = sum([a*b for a,b in zip (patternlist[j],datalist)])
		calculate newmaxi, which is the new maximum of the sum of the current row and pattern's output and the maximum of compatible 
		patterns' outputs for the previous row 
		updating the corresponding grid in answergrid to store the new maximum value
		
Its running time is O(n) because there's a for loop looping through every element in in n rows in the input file table, the other for
loop only loops through the eight patterns.

c) The maximum value of a valid placement for this sample grid is 10753. 

Short transcript of the program in operation:

With the given grid.txt as the input, the program prints:
The maximum value of a valid placement for this sample grid is 10753.0. 