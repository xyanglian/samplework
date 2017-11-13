'''
Created on Nov 16, 2015

@author: xiaoyuyanglian
'''
def most(words):
    answer = []
    lst = []
    for word in words:
        lst.append(words.count(word))
     
    for word in words:
        if words.count(word) == max(lst):
            answer.append(word)    
            
    if len(answer) > 1:
        return sorted(answer)[-1]
          
    return answer[0]