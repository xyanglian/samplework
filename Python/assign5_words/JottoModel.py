'''
Created on Oct 29, 2015

@author: xiaoyuyanglian
'''
global allWords
#global variable for all the words read when loadWords is called
global changeWords
#global variable for the words that change as the game is played 
global counts
#global variable for the number of guesses made 
import random 
#imports random 

def loadWords(filename):
    #loads words from specified file into a global list 
    global allWords
    f = open(filename)
    st = f.read()
    allWords = st.split()
    #error checking

def getGuess():
    # returns random string chosen from appropriate global variable and updates global count of number of guesses
    global changeWords
    global counts 
    guess = random.choice(changeWords)
    counts += 1 
    return guess 
    
def guessCount():
    #returns number of guesses made in model
    global counts
    return counts

def startGame():
    # initializes global variables used in playing one game
    global allWords
    global changeWords
    global counts
    counts = 0
    changeWords = allWords[:] 

def common(a,b):
    # returns number of letters in common between given strings a and b, regardless of the location of those letters vis-a-vis the strings

    alist = list(a)
    blist = list(b)
    for c in alist:
        if c in blist:
            blist[blist.index(c)] = '*'
    return blist.count("*")

def processCommon(guess, count):
    # uses list comprehension to set global variable to only those words that have count letters in common with guess and removes guess from global variable
    
    global changeWords
    
    changeWords = [w for w in changeWords if common(w,guess) == count and w != guess]
    return len(changeWords)
    