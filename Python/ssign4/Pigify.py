'''
Created on Sep 17, 2015

@author: Liane Yanglian
'''
def pigword(word):
    # converts a word into pig-latin according to the rules given by the requirements
    vowellist = ["a","e","i","o","u","A","E","I","O","U"]
    if word[0] in vowellist:
        return word + "-way"
    if word[0] == "q" or word[0] == "Q":
        return word[2:] + "-quay"
    for ch in word:
        if ch not in vowellist:
            return word + "-way"    
    else:
       for ch in word:
           if ch in vowellist:
               return word[word.find(ch):] + "-" + word[:word.find(ch)] + "ay"

def unpigword(word):
    # converts a word from piglatin back to the English word
    vowellist = ["a","e","i","o","u","A","E","I","O","U"]
    if word[0] in vowellist and word.endswith("-way"):
        return word [:-4]
    if word[0] in vowellist or word [0] == "y" and not word.endswith("-way"):
        return word[(word.find("-")+1):word.find("ay")] + word[:word.find("-")] 
    if word.endswith("-way") and word[0] not in vowellist:
        return word [:-4]    
    elif word.endswith("-quay"):
            return "qu" + word[:-5] 
    
def pigall(st):
    # takes a string as a parameter and returns a string that consists of each word in the original string turned into piglatin
    all = []
    for word in st.split():
        all.append(pigword(word))
    return ' '.join(all)

def unpigall(st):
    # takes a string as a parameter and returns a string that consists of each word in the original string translated back from piglatin into English
    all = []
    for word in st.split():
        all.append(unpigword(word))
    return ' '.join(all)

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
    # start with reading in data file
    word = readFile("romeo.txt")
    print "read",len(word),"words"
    result = ' '.join(word)

    # convert to piglatin and write to file
    pigstr = pigall(result)
    writeFile(pigstr.split(),"pig-romeo.txt")
    print "PIGIFIED romeo.txt"
    print pigstr[0:100]

    # read in pigified file
    st = readFile("pig-romeo.txt")
    print "read", len(st), "st"
    results = ' '.join(st)
    # unpigify file that was read
    unpigstr = unpigall(results)
    # write to file "unpig-romeo.txt"
    writeFile(unpigstr.split(), "unpig-romeo.txt")
    print "UNPIGIFIED romeo.txt"
    print unpigstr[0:100] 

