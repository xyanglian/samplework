'''
Created on Nov 10, 2015

@author: xiaoyuyanglian
'''
def freqs(data):
    st = sorted(data)
    lst = []
    wordlist = []
    for word in st:
        if word not in wordlist:
            wordlist.append(word)
            lst.append(st.count(word))

    return lst