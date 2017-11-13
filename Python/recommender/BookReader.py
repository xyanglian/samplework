'''
Created on Dec 3, 2015

@author: Liane Yanglian & Linda Zhou
'''
import json

def readDatafile (filename):
    # given a filename that is formatted as comma separated values, return a list of lists of strings, where each line is represented as a list of separate string elements
 
    f = open(filename)
    result = [ line.strip().split(',') for line in f.readlines() if len(line) > 1 ]
    f.close()
    return result

def convertStrings (statList):
    # returns a list of integers, the converted values of the strings, given a list of string representing integer values

    return [ int(s) for s in statList ]



def getData (filename):
    # given the name of a file of data about restaurant ratings, returns two sequences: a list of strings, the restaurant names in file order,and a dictionary of strings as the key and a list of integers as the values, the raters and their ratings of the books

    data = readDatafile(filename)
    
    listofitems = []
    
    Dofratings = {}
    for line in data:
        rater = line[0]
        ratings=[]
        idx=1
        while idx < (len(line)-1):
            ratings.append(line[idx + 1])
            idx= idx + 2
        ratings = convertStrings(ratings)
        Dofratings[rater] = ratings
    idx=1
    while idx < (len(data[0])-1):
            listofitems.append(data[0][idx])
            idx= idx + 2
            
    return (json.dumps(listofitems), json.dumps(Dofratings))

if __name__ == "__main__":
    # main function that calls getData(filename) 
    (items,ratings) = getData("bookratings.txt")
    print"items = ",items
    print"ratings = ", ratings
    
    print type(items), type(ratings)
    var = json.loads(items)
    print type(var),var
    dvar = json.loads(ratings)
    print type(dvar),dvar