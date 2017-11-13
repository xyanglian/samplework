'''
Created on Sep 10, 2015

@author: xiaoyuyanglian
'''

phrase = "Do Re Me Fa So La Ti Do"
def acronym(phrase): 
    phraseList = phrase.split()    
    answer = ""
    for word in phraseList:
        answer = answer + word[0]
    return answer
        
print acronym(phrase)


