'''
Created on Oct 6, 2015

@author: Liane Yanglian
'''
import random
#imports random

def getWords():
    #loads words from specified file
    f = open("kwords5.txt")
    st = f.read()
    words = st.split()
    #error checking
    for w in words:
        if len(w) != 5:
            print "error:",w
    return words

def common(a,b):
    # returns number of letters in common between given strings a and b regardless of the location of those letters vis-a-vis the strings

    alist = list(a)
    blist = list(b)
    for c in alist:
        if c in blist:
            blist[blist.index(c)] = '*'
    return blist.count("*")

def play(words):
    # sets the rules for the game and uses a list comprehension that creates a new list which is assigned to the variable words
    print "Jotto: Think of a five-letter word, I'll guess your word"
    print "enter number of letters in common, 6 if correct word"
    count = 0
    while True:
  
        guess = random.choice(words)
 
        print "I'm considering",len(words),"different words"
        print "my guess:",guess
        same = raw_input("how many in common (6 if word guessed)? ")
        sameInt = int(same)
        if sameInt == 6:
            print "I win!!"
            break
        words = [w for w in words if common(w,guess) == sameInt and w != guess]
        if len(words) == 0:
            print "error: we've run out of words and your word hasn't been guessed"
            break
        count += 1
    print "the number of words guessed: " + str(count)
    print "thank you for playing Duke Jotto"

if __name__ == '__main__':
    # main function that calls play(words) and executes the game 
    words = getWords()
    print "read",len(words),"words"
    play(words)