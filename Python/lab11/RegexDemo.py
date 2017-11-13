'''
Created on Nov 29, 2015

'''
import re

def getmatches(pattern,words):
    ret = []
    for w in words:
        try:
            m = re.search(pattern,w)
            if m:
                ret.append(w)
        except:
            print 'malformed pattern:',pattern
            break
    return ret
   
def loopmatch(words):
    while True:
        pattern = raw_input('enter pattern> ')
        if len(pattern) == 0:
            break
        matches = getmatches(pattern,words)
        for m in matches:
            print m
        print "# matches:",len(matches), 'for pattern:',pattern
            

if __name__ == '__main__':
    f = open("words.txt")
    words = [line.strip() for line in f]
    loopmatch(words)
