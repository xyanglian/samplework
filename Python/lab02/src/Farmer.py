'''
Date: Sept 2-3, 2015

@author: Liane Yanglian and Linda Zhou 
'''

def hiho():
    print "Hi-ho, the derry-o"
def farmer():
    print "The farmer in the dell"
cheese = "cheese stands alone"

def song():
    farmer() 
    farmer()  
    hiho()
    farmer()
    print
    part()
    last()
    verse("mouse","cheese")

    
word = ["farmer", "wife", "child","nurse", "dog", "cat", "mouse", "cheese" ]
def part():
    for i in range(7):
        print "And the",word[i],"takes the", word[i+1]
        print "The", word[i],"takes the", word[i+1]
        hiho()
        print "The", word[i],"takes the", word[i+1]
        print

def last():
    print "And the",cheese
    print "The",cheese
    hiho()
    print "The",cheese
    print

def verse(taker,thing):
    print "And the",taker,"takes the",thing
    print "The",taker,"takes the",thing
    hiho()
    print "The",taker,"takes the",thing
    print
     
if __name__ == '__main__':
    song()
