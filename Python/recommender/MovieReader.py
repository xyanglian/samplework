'''
Created on Dec 3, 2015

@author: Liane Yanglian & Linda Zhou
'''

import json

def readDatafile (filename):
    #reads data from a specifc file
    f = open(filename)
    result = [ line.strip().split(',') for line in f if len(line) > 1 ]
    f.close()
    return result

def getData (filename):
    # given the name of a file of data about restaurant ratings, returns two sequences: a list of strings, the restaurant names in file order,and a dictionary of strings as the key and a list of integers as the values, the raters and their ratings of the books

    data = readDatafile(filename)
    
    listofitems = []  
    ratingsDict = {}
    for line in data:
        if line[1] not in listofitems:
            listofitems.append(line[1])
    listofitems.sort()
    for line in data:
        movie = line[1]
        rater = line[0]
        if rater not in ratingsDict:
            ratingsDict[rater] = [0]*len(listofitems)
        i = listofitems.index(movie)
        ratingsDict[rater][i] = int(line[2])
            
    return (json.dumps(listofitems), json.dumps(ratingsDict))
if __name__ == "__main__":
    # main function that calls getData(filename) 
    (items,ratings) = getData("movieratings.txt")
    print"items = ",items
    print"ratings = ", ratings
    
    print type(items), type(ratings)
    variable = json.loads(items)
    print type(variable),variable
    dvariable = json.loads(ratings)
    print type(dvariable),dvariable