'''
Created on Sep 28, 2015

@author: Liane Yanglian
'''
from posix import lstat

def is_alpha(word):
    # determines if a string is an alphabetic character because the program is only supposed to transform alphabetic characters, not others.
    for ch in word:
        if not ch.isalpha():
            return False
    return True

def shiftword(word,shift): 
    # shifts characters and encrypts characters and assembles encrypted characters into a string
    alph   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphsmall = "abcdefghijklmnopqrstuvwxyz"
    caesar = alph[shift:]+alph[:shift]
    caesarsmall = alphsmall[shift:]+alphsmall[:shift]
    desired = []
    for i in word:
        if i in alph:
            findex=alph.find(i)
            message = caesar[findex]
            desired.append(message)
        if i in alphsmall: 
            findex=alphsmall.find(i)
            message = caesarsmall[findex]
            desired.append(message)
    return "".join(desired)
 
def encrypt(str, shift):
    # breaks the string into a list of words, encrypts each word, and reassembles the encrypted words into a string
    all = []
    for word in str.split():
        all.append(shiftword(word,shift))
    return ' '.join(all)

def eyeball(encrypted):
    # prints 26 rows labeled with the value of the shift being applied
    for i in range (26):
        print str(i) + " " + encrypt(encrypted,i)[0:80]


def alphaFreq(inputString):
    # give a list of the number of times each character, in both its upper and lower cases, has occurred in a text 
    lst = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ch in alphabet:
        lst.append(inputString.count(ch) + inputString.count(ch.upper()))    
    return lst

def chisquare(encrypted):
    # uses the chi-square formula to find the shift which has the smallest chi-suared value from calculating chi-square from each of the possible 26 shifts from 0-25 and uses the minimal of these to return the shift that generates the minimal value 
    freqs = [8.04, 1.48, 3.34, 3.82, 12.49, 2.40, 1.87, 5.05, 7.57, 0.16, 0.54, 4.07, 2.51, 7.23, 7.64, 2.14, 0.12, 6.28, 6.51, 9.28, 2.73, 1.05, 1.68, 0.23, 1.66, 0.09]
    numLetters = sum(alphaFreq(encrypted))
    expected_freqs = []
    
    for i in range(26):
        expected_freqs.append(numLetters * freqs[i]/100)
    
    chisquare = []
    for shift in range(26):
        shiftedstring = shiftword(encrypted, shift)
        observedFreqs = alphaFreq(shiftedstring)
        totalscore = 0
        for i in range(26):
            Ei = expected_freqs[i]
            numerator = (observedFreqs[i] - Ei)**2
            denominator = Ei
            totalscore += (numerator/denominator)
        chisquare.append(totalscore)
    print chisquare.index(min(chisquare))
    print chisquare
    return chisquare.index(min(chisquare))
    
def readFile(fname):
    # returns a list of words read from file specified by fname
    f = open(fname)
    st = f.read()
    f.close()
    return st.split()

def writeFile(words, fname):
    # writes every element in words, a list of strings, to the file whose name is fname; puts a space between every word written, and makes lines have length 80
    LINE_SIZE = 80
    f = open(fname,"w")
    wcount = 0
    for word in words:
        f.write(word)
        wcount += len(word)
        if wcount + 1 > LINE_SIZE:
            f.write('\n')
            wcount = 0
        else:
            f.write(' ')
    f.close()


if __name__ == '__main__':
    # starts with reading in data file
    word = readFile("romeo.txt")
    print "read",len(word),"words"
    result = ' '.join(word)

    # encrypts the file and writes to file
    ceasarstring = encrypt(result,19)
    writeFile(ceasarstring.split(),"crypt-romeo.txt")
    print "caesar:crypt-romeo.txt"
    print ceasarstring[0:80]
    
    # reads file and print 26 rows to examine the original message
    word = readFile("file1.txt")
    result = ' '.join(word)
    eyeball(result)
    
    # reads file calls the function chi-square with the file and prints the result returned by the function and the result of decrypting with the returned value
    word = readFile("file2.txt")
    result = ' '.join(word)
    chisquare(result)
    

    
    




    
    
    