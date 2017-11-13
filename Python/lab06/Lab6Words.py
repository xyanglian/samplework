'''
Created on Oct 4, 2015

@author: Liane Yanglian
'''
def readWords():
    f = open("lowerwords.txt")
    return f.read().split()

def countLen(words, length):
    l=0
    for w in words:
        if len(w) == length:
            l+=1
    return l

    '''
    return the number of strings in words whose length is 
    the value of parameter length. So if length is 3, this is
    the number of 3-letter strings in words
    '''


def stars(num):
    strings = "*"
    if num/150 != 0:
        stars = num/150
        return stars*strings
    else: 
        return strings
    '''
    returns a string containing one asterisk for each time
    num is fully divisible by 150, e.g., num/150 asterisks. 
    If this is zero, return a string with a single asterisk
    '''
def wordLengths(words):
    total = 0
    for length in range(1,33):
        val = countLen(words,length)
        total += val
        if val > 0:
            print length, "\t", val, "\t", stars(val)
    return total

if __name__ == '__main__':
    words = readWords()
    print "read",len(words),"words"
    total = wordLengths(words)
    print "value returned",total
