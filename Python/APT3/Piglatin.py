s'''
Created on Sep 18, 2015

@author: xiaoyuyanglian
'''

def convert(s):
    vowellist = ["a","e","i","o","u"]
    if s[0] in vowellist:
        return s + "-way"
    if s[0] == "q":
        return s[2:] + "-quay"
    else:
       for ch in s:
           if ch in vowellist:
               return s[s.find(ch):] + "-" + s[:s.find(ch)] + "ay"
    
            
    
    
        
     

