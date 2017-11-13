'''
Created on Oct 29, 2015

@author: xiaoyuyanglian
'''
import random
#imports random
def loadWords(filename):
    # reads words from specified file and returns a list of strings, with each string being one line of the file

    allwords = []
    f = open(filename)
    for line in f:
        line = line.strip()
        allwords.append(line)
    f.close()
    return allwords
    
     
def getWords(allwords):
    # returns a list of words having a specified length from allwords 

    wlist = [w for w in allwords]
    return wlist

def display(guess):
    # creates a string from list guess to print and show the player

    return ' '.join(guess)

def makeSecretList(secret):
    # creates the list that's modifiable to track letters guessed by the player and creates "_" entries only for alphabetic characters

    empty = []
    for ch in secret:
        if ch.isalpha():
           empty.append('_')
        else:
            empty.append(ch)
    return empty 
            

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
        print "letters not guessed: " + " ".join(alp)
        
    if guess.count("_") == 0:
        print "word is guessed!",word
    else:
        print "you lost! word is",word
        
def play(allwords):
    # calls the function doGame(word)
    words = getWords(allwords)    
    word = random.choice(words)
    doGame(word)

if __name__ == '__main__':
    # main function that calls the other functions by first asking the player to choose which category s/he wants to guess and calls the function play(allwords)
    wlen = str(raw_input("which category do you want to guess? Songs or normal (normal is guessing normal words)? ")) 
    if wlen == "Songs":
        allwords = loadWords("songs.txt")
    if wlen == "normal":
        allwords = loadWords("lowerwords.txt")
    play(allwords)
    