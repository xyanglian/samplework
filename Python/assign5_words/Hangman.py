'''
Created on Oct 18, 2015

@author: Liane Yanglian
'''
import random
#imports random
from encore.storage.tests.static_url_store_test import count
#imports count

def loadWords(filename):
    # loads all words from specified file and returns a list of strings with each string being one line of the file

    allwords = []
    f = open(filename)
    for line in f:
        line = line.strip()
        allwords.append(line)
    f.close()
    return allwords
    
     
def getWords(allwords,wordlength):
    # returns a list of words having a specified length from allwords

    wlist = [w for w in allwords if len(w) == wordlength]
    return wlist

def display(guess):
    # creates a string from list guess to print and show the player

    return ' '.join(guess)

def makeSecretList(secret):
    # creates the list that's modifiable to track letters guessed by the player 

    return ['_']*len(secret)

def doGame(word):
    # sets the rules of the game while keeping count of the number of misses,the letters guessed and not guessed, and breaks the while loop after 8 guesses
    guess = makeSecretList(word)
    miss = 0
    count = 8
    lg = []
    alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while True:
        if guess.count('_') == 0:
            break
        if count == 0:
            break 
        print "secret so far:",display(guess)
        letter = raw_input("guess a letter: ")
        for index in range(len(word)):
            if word[index].lower() == letter.lower():
                guess[index] = word[index]
        if letter.lower() not in word.lower() and letter.lower() not in lg:
            lg.append(letter.lower())
            miss += 1
            count -= 1 
        print "number of misses already had:" + str(miss)
        print "number of misses left: " + str(count)
        print "letters guessed: " + " ".join(set(lg))
        for el in alp:
            if letter.lower() == el:
                alp.remove(el)
        print "letters not yet guessed: " + " ".join(alp)
        
    if guess.count("_") == 0:
        print "word is guessed!",word
    else:
        print "you lost! word is",word
 
def play(allwords):
    # calls the function doGame(word) and asks the player for input about the number of letter they would like to guess 
    wlen = int(raw_input("how many letters in word you'll guess? "))
    words = getWords(allwords,wlen)    
    word = random.choice(words)
    doGame(word)

if __name__ == '__main__':
    # main function that executes the game and calls the function play(allwords)
    allwords = loadWords("lowerwords.txt")
    play(allwords)