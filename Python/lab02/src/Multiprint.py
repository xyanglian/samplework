'''
Date: Sept 2-3, 2015

@author: Linda Zhou and Liane Yanglian
'''


word = "wonderful"
count = 1

def printit():
    global count,word
    print count,"\t",word
    count = count + 1

def f1():
    printit()
    printit()
    
def f2():
    f1()
    f1()
    
def f3():
    f2()
    f2()

def f4():
    f3()
    f3()

def f5():
    f4()
    f4()

def f6():
    f5()
    f5()
    
def f7():
    f6()
    f6()
    
def verse():
    f7()
    f7()
    
if __name__ == "__main__":
    verse()
