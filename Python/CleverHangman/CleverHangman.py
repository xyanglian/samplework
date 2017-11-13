'''
Created on Nov 18, 2015

@author: xiaoyuyanglian
'''
import random


def load_lines(filename):
    """
    reads words from specified file and returns a list of
    strings, each string is one line of the file
    
    """
    lines = []
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        lines.append(line)
    return lines

def getwords(filename, wordlength):
    """
    returns a list of words having a specified length from
    the file whose name is filename.
    
    """
    lines = load_lines(filename)
    wlist = [w for w in lines if len(w) == wordlength]
    return wlist

def numguess():
    "sets the number of guesses"
    print "Please set number of guesses: " , 
    numguesses = raw_input()
    numguesses = int(numguesses)
    while numguesses > 26 or numguesses == 0:
        print
        print "Please choose integer value between 0-26, non-inclusive."
        numguesses = raw_input()
        numguesses = int(numguesses)

    return numguesses
    
def prolet(guessed,secret,letter):
    "Checks the letterguessed with secret"
    letterle = letter.lower()
    secretle = secret.lower()
    for chl in range(len(secretle)):
        if secretle[chl] == letterle:
            guessed[chl] = letterle
            
    return guessed

def whatlength():
    "starting the setup for cleverhangman"
    print "What to do?"
    print "1. Please guess only letters and letters that have not been guessed already."
    print "2. The number of guesses is between 1 and 15 inclusive."
    print "Please choose word length (between 3 to 10 inclusive) :  "
    answer = raw_input()
    answer = int(answer)
    codelist = getwords("lowerwords.txt", answer)
    randu = random.randint(0,len(codelist))
    codeword = codelist[randu]
    
    return answer

def categorize(alpha,wordlst,guessed):

    "creates a dictionary  places words into categories and generates the number of words for each category"
    
    d={}
    for word in wordlst:
        keylist=[]
        for index in range(len(word)):
            
            if word[index].lower() == alpha.lower():
                keylist.append(alpha.lower())
            "helps to update the keys with current gslst"
            if word[index].lower() == guessed[index]:
                keylist.append(word[index].lower())
            else:
                keylist.append("_")
        key = "".join(keylist)
        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]
    return d

def optimize(dictionary):
    "chooses the key with the largest length"
    max = 0
    value = []
    for item in dictionary.keys():
        if len(dictionary[item]) > max:
            max = len(dictionary[item]) 
            value = dictionary[item]
    return value

def start():
    "allows player to choose which mode to play"
    print "Welcome to Hangman!"
    print "Do you want to play in the Game Mode (g) or Test Mode (t)?"
    print "Type g or t:"
    category = raw_input().lower()
    
    if category == "g":
        playmode()
        
    if category =="t":
        testmode()
        
def playmode():
    "same as testmode, which sets up the game, but without the additional information"
    letterguessed = ""
    alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    gslst =[]
    currentlist = getwords("lowerwords.txt", whatlength())
    secret = random.choice(currentlist)
    for i in range(len(secret)):
        gslst.append("_")
    d = categorize("!",currentlist,gslst) 
    currentlist = optimize(d)

    guesscount = numguess()
    guessleft = guesscount
    guesses = []
    
    "this is the setup"
    print "number of words possible:" , len(d["".join(gslst)])
    print
    print "The word is" , "".join(gslst)
    print "Guesses left: ", guessleft
    print "Guesses made: ", ",".join(guesses)
    for letter in guesses:
        if letter in guesses and letter.lower() in alph:
            alph.remove(letter.lower()) 
    print "Letters to guess: ", ",".join(alph)

    "loops through all guesses"
    while "".join(gslst) != secret.lower():
        letterguessed = raw_input() 
        dict = categorize(letterguessed, currentlist,gslst)
        currentlist = optimize(dict)
        secret = random.choice(currentlist)  
        if len(letterguessed) ==1 and letterguessed in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" and letterguessed.lower() not in guesses:
            prolet(gslst,secret,letterguessed)
            guessleft -=1
            guesses.append(letterguessed.lower())
            if letterguessed.lower() not in secret.lower():
                print
                print
                print "The letter", letterguessed,"is not in the word."

            print
            print
            print
            print "number of words possible:" , len(currentlist)
            print "The word is" , "".join(gslst)
            print "Guesses left: ", guessleft
            print "Guesses made: ", ",".join(guesses)
            for letter in guesses:
                if letter in guesses and letter.lower() in alph:
                    alph.remove(letter.lower()) 
            print "Letters to guess:", ",".join(alph)

            if guessleft == 0 and "".join(gslst) != secret.lower():
                print
                print
                print "Uh oh,you are hung! The word was", secret,"."
                break
            
        elif len(letterguessed) > 1:
            prolet(gslst,secret,letterguessed)
            guessleft -=1
            guesses.append(letterguessed.lower())
            if letterguessed.lower() not in secret.lower():
                print
                print
                print "The letter", letterguessed,"is not in the word."
                
            print "The word is" , "".join(gslst)
            print "Guesses left: ", guessleft
            print "Guesses made: ", ",".join(guesses)
            for letter in guesses:
                if letter in guesses and letter.lower() in alph:
                    alph.remove(letter.lower()) 
            print "Letters to guess: ", ",".join(alph)
            print ""
            
            if letterguessed.lower() == secret.lower():
                print
                print "Congratulations! The word is" , secret,".","You managed to guess it in",guesscount-guessleft, "tries!"
                break
            
        else:
            print "Please do not guess non-letters or letters already guessed!"
      
        
    if "".join(gslst) == secret.lower() or letterguessed == secret.lower():     
        print
        print "Congratulations! The word is" , secret,".","You managed to guess it in",guesscount-guessleft, "tries!"
            
def testmode():
    "sets up the game for testing purposes, which shows how the game runs with the additional information not available in gamemode"

    letterguessed = ""
    alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    gslst =[]
    currentlist = getwords("lowerwords.txt", whatlength())
    secret = random.choice(currentlist)
    for i in range(len(secret)):
        gslst.append("_")
    d = categorize("!",currentlist,gslst) 
    currentlist = optimize(d)

    guesscount = numguess()
    guessleft = guesscount
    guesses = []
    
    "this is the setup"
    print "(Secret word:",secret,")"
    print "number of words possible:" , len(d["".join(gslst)])
    print
    print "The word is" , "".join(gslst)
    print "Guesses left: ", guessleft
    print "Guesses made: ", ",".join(guesses)
    for letter in guesses:
        if letter in guesses and letter.lower() in alph:
            alph.remove(letter.lower()) 
    print "Letters to guess: ", ",".join(alph)
    print "Dictionary of categories and number of words:"

    "loops through all guesses"
    while "".join(gslst) != secret.lower():
        letterguessed = raw_input() 
        "Choose secret word from dict"
        dict = categorize(letterguessed, currentlist,gslst)
        currentlist = optimize(dict)
        secret = random.choice(currentlist)  
        "When letter is not in the word"
        if len(letterguessed) ==1 and letterguessed in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" and letterguessed.lower() not in guesses:
            prolet(gslst,secret,letterguessed)
            guessleft -=1
            guesses.append(letterguessed.lower())
            if letterguessed.lower() not in secret.lower():
                print
                print
                print "The letter", letterguessed,"is not in the word."
                
            print
            print
            print
            print "(Secret word:",secret,")"
            print "number of words possible:" , len(currentlist)
            print "The word is" , "".join(gslst)
            print "Guesses left: ", guessleft
            print "Guesses made: ", ",".join(guesses)
            for letter in guesses:
                if letter in guesses and letter.lower() in alph:
                    alph.remove(letter.lower()) 
            print "Letters to guess: ", ",".join(alph)
            print "Dictionary of categories and number of words:"
            for item in dict.keys():
                print item,
                print len(dict[item])
            "When you run out of tries"
            if guessleft == 0 and "".join(gslst) != secret.lower():
                print
                print
                print "Uh oh,you are hung! The word was", secret,"."
                break
        "When the guessed letter is not a letter but a word"
        if len(letterguessed) > 1:
            prolet(gslst,secret,letterguessed)
            guessleft -=1
            guesses.append(letterguessed.lower())
            if letterguessed.lower() not in secret.lower():
                print
                print
                print "The letter", letterguessed,"is not in the word."
                
            print "The word is" , "".join(gslst)
            print "Guesses left: ", guessleft
            print "Guesses made: ", ",".join(guesses)
            for letter in guesses:
                if letter in guesses and letter.lower() in alph:
                    alph.remove(letter.lower()) 
            print "Letters to guess: ", ",".join(alph)
            print ""
            "When you guess the whole correct word"
            if letterguessed.lower() == secret.lower():
                print
                print "Congratulations! The word is" , secret,".","You managed to guess it in",guesscount-guessleft, "tries!"
                break
            
        else:
            print "Please do not guess non-letters or used letters!"
      
        
    if "".join(gslst) == secret.lower() or letterguessed == secret.lower():     
        print
        print "Congratulations! The word is" , secret,".","You managed to guess it in",guesscount-guessleft, "tries!"

if __name__ == "__main__":
    "main function that calls the function start()"
    start()


    org = [(g,h[0],h[1]) for g,h in d.iteritems()]
    sort = sorted(org, key = itemgetter(2), reverse = False)
    sortt = sorted(sort, key = itemgetter(1), reverse = True)
    final = [g for (g,p,q) in sortt]