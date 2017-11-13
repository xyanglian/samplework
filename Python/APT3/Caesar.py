'''
Created on Sep 18, 2015

@author: xiaoyuyanglian
'''
def decode(cipher, shift):
    str = ""
    for ch in cipher:
        if ord(ch) - shift < 65:
            str += chr(91- (shift - (ord(ch) - 65)))
        else:
            str += chr(ord(ch)-shift)
    return str
