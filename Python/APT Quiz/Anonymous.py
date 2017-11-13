'''
Created on Nov 3, 2015

@author: xiaoyuyanglian
'''

def check(messages, headlines):
    new = list("".join(headlines).lower())
    for i in range(len(messages)):
            for letter in list(messages[i]):
                if letter.lower() in new:
                    new.remove(letter.lower())
    
def howMany(headlines,messages):
    count = 0
    lst = []
    new = list("".join(headlines).lower())

    
    for i in range(len(messages)):
        messages [i] = messages[i].split()
        if check (messages[i],headlines) == True:
            count += 1
                 
    
    return count 
