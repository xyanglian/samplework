'''
Created on Sep 13, 2015

@author: Liane Yanglian and Sarah Du 
'''
def alpha_rotate(n):
    s = "abcdefghijklmnopqrstuvwxyz"
    ret = s[n:] + s[:n]
    return ret

def encrypt(source,n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    code = alpha_rotate(n)

    newlets = [code[alpha.index(ch)] for ch in source]
    return ''.join(newlets)


if __name__ == '__main__':  
    s = "freud"
    us = encrypt(s,23)
    print us
