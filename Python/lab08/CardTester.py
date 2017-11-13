'''
Created on Feb 14,2011
@author: Liane Yanglian and Sarah Du 
'''

import random

def toCardString(card):
    rankStrings = ["ace","two","three","four","five","six","seven",
                   "eight","nine","ten","jack","queen","king"]
    suitStrings = ["spades", "hearts", "diamonds","clubs"]
    return rankStrings[card[0]] + " of " + suitStrings[card[1]]

def get_rank_counts(hand):
    '''
    returns list of how often each rank 1-13 occurs in a hand
    e.g., list[3] = # occurrences of a 3, list[11] = # occurrences of jack
    '''
    counts = [0]*13
    for card in hand:
        rank = card[0]
        counts[rank] += 1
    return counts

def get_suit_counts(hand):
    counts = [0]*4
    for card in hand:
        suit = card[1]
        counts[suit] += 1
    return counts

def one_pair(hand):
    '''
    Return true if hand has exactly one pair
    '''
    ranks = get_rank_counts(hand)
    if ranks.count(2) == 1 and ranks.count(1) == 3:
        return True
    return False

def two_pair(hand):
    ranks = get_rank_counts(hand)
    if ranks.count(2) ==2 and ranks.count(1) == 1:
        return True 
    return False 

def three_kind(hand):
    ranks = get_rank_counts(hand)
    if ranks.count(3) ==1 and ranks.count(1) == 2:
        return True
    return False

def fullhouse(hand):
    ranks = get_rank_counts(hand)
    if ranks.count(3) ==1 and ranks.count(2) == 1:
        return True
    return False


def flush(hand):
    suits = get_suit_counts(hand)
    if suits.count(5) ==1:
        return True
    return False 
    
def get_deck():
    '''
    create and return an unshuffled deck of cards
    '''
    d = []
    for rank in range(0,13):
        for suit in range(0,4):
            d.append([rank,suit])
    return d

def get_hand(deck):
    random.shuffle(deck)
    return deck[0:5]

def print_hand(hand):
    print '[',
    for card in hand:
        print toCardString(card),',',
    print ']'
    

def deal_demo():
    deck = get_deck()
    print_hand(deck)
    print_hand(get_hand(deck))
    print_hand(get_hand(deck))

def funcstring(funcname):
    s = str(funcname)[10:]  #chop off '<function '
    spi = s.index(' ')
    return s[:spi]

def simulate(n,hand_type):
    '''
    Simulate dealing n poker hands, return number
    of times that hand_type occurs, where handType could
    b is_pair or is_flush or ...
    '''
    deck = get_deck()
    pc = 0
    for i in range(0,n):
        hand = get_hand(deck)
        if hand_type(hand):
            pc += 1
    print "# hands = %d, # %s = %d, prob = %.5f" % (n, funcstring(hand_type),pc, 1.0*pc/n)
    
if __name__ == "__main__":
    #deal_demo()
    hands = 20000
    simulate(hands,fullhouse)
    #simulate(hands,three_kind)
    #simulate(hands,two_pairs)
    #simulate(hands,full_house)
    #simulate(hands,four_kind)
    #simulate(hands,flush)
