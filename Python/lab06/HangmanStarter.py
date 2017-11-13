'''
Created on Oct 4, 2015

@author: Liane Yanglian
'''

def guessLetters(word):
    guess = ['_']*len(word)
    miss = 0
    
    while True:
        print "guessing", ''.join(guess)
        letter = raw_input("guess a letter: ")
        if letter in guess:
            print "this letter was already guessed"
        else:  
            for index in range(len(word)):
                if word[index] == letter:
                    guess[index] = letter
                    print "you guessed a letter"
                
        if letter not in word:
            print "that's a miss"
            miss += 1
        if guess.count('_') == 0:
            print "number of misses:", miss
            break
        

if __name__ == '__main__':
    guessLetters("fabulous")