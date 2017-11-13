'''
Created on Sep 2, 2015

@author: ola
'''
def pluralize(word):
    ret = word + "s"
    if (word.endswith("ch")):
        ret = word + "es"
    if (word.endswith("x")):
        ret = word + "es"
    if (word.endswith("f")):
        ret = word[:-1] + "ves"
    if (word.endswith("y")):
        ret = word[:-1] + "ies"
    return ret
        
if __name__ == "__main__":
    words = ["phone","book","baby","punch","fox","elf","country","sun"]
    for w in words:
        print w, pluralize(w)