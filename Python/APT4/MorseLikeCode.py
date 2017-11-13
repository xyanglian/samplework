'''
Created on Sep 29, 2015

@author: xiaoyuyanglian
'''
def decrypt(library,message):
    letters = []
    encryption = []
    for notation in library:
        z = notation.split()
        letters.append(z[0])
        encryption.append(z[1])
        
    translation = []
    for element in message.split():
        if element in encryption:
            translation.append(letters[encryption.index(element)])
        else:
            translation.append("?")
    return "".join(translation)
          
    
    
    
