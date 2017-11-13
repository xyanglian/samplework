'''
Created on Sep 10, 2015

@author: lianeyanglian
'''
def hair_long():
    # makes long hair
    return r"|||||||||||||||||" + "\n"

def eyes_normal():
    # makes normal-looking eyes
    a1 = r"  ----     ----  "
    a2 = r" /    \   /    \ "
    a3 = r"    o  | |  o    "
    a4 = r" \    /   \    / "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4

def ears_normal():
    # makes normal-looking ears
    return r"-               -"

def nose_small():
    # makes a small nose
    return r"|       |       |"
   
def mouth_smiley():
    # makes a smiley mouth
    return r"|    \_____/    |"

def chin_fat():
    # makes a fat chin
    a1 = r"|               |"
    a2 = r"\_______________/"
    return a1 + "\n" + a2

def hair_morning():
    # makes messy hair like that you have after waking up
    return r"|||\\||||\\||||\\|" + "\n"

def eyes_leftlooking():
    # makes eyes that look to the left
    a1 = r"  ----     ----  "
    a2 = r" /    \   /    \ "
    a3 = r"  o    | | o     "
    a4 = r" \    /   \    / "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4

def ears_round():
    # makes round ears
    return r"o               o"

def nose_bignostrils():
    # makes a nose with conspicuous nostrils
    return r"|      \|       |"

def mouth_grumpy():
    # makes a mouth that looks grumpy
    return r"|    /-----\    |"

def chin_long():
    # makes a long chin
    a1 = r"|               |"
    a2 = r"|               |"
    a3 = r"\_______________/"
    return a1 + "\n" + a2 + "\n" + a3

def hair_reverse():
    # makes hair that's reversed
    return r"\\\\\\\\\\\\\\\\\\" + "\n"

def eyes_rightlooking():
    # makes eyes that look to the left
    a1 = r"  ----     ----  "
    a2 = r" /    \   /    \ "
    a3 = r"     o | |    o  "
    a4 = r" \    /   \    / "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4

def ears_twoholes():
    # makes ears that are essentially two holes
    return r":               :"

def nose_big():
    # makes a nose that's very big
    return r"|       |||     |"
   
def mouth_full():
    # makes a mouth that's full
    return r"|    \-----/    |"

def chin_weird():
    # makes a chin that looks weird
    a1 = r"|               |"
    a2 = r"/_______________/"
    return a1 + "\n" + a2

def hair_badhaircut():
    # makes hair that is a result of bad hair cut like we all have once in a while
    return r"\\\\\// \\\/\\\ \\" + "\n"

def eyes_crosseyes():
    # makes funny crossed eyes 
    a1 = r"  ----     ----  "
    a2 = r" /    \   /    \ "
    a3 = r"      o| |o      "
    a4 = r" \    /   \    / "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4

def ears_earrings():
    # makes ears that wear earrings
    return r"{               }"

def nose_fourholes():
    # makes no nose
    return r"|      ::       |"
   
def mouth_mustachecovered():
    # makes a mouth with mustache
    return r"|    \|||||/    |"

def chin_square():
    # makes a chin that's square-shaped
    a1 = r"|               |"
    a2 = r"|_______________|"
    return a1 + "\n" + a2

def totem ():
    # prints three different heads
    # the first head of the totem pole
    print hair_long()
    print eyes_normal()
    print ears_earrings()
    print nose_small()
    print mouth_smiley()
    print chin_fat()
    # the second head of the totem pole
    print hair_reverse()
    print eyes_rightlooking()
    print ears_normal()
    print nose_big()
    print mouth_full()
    print chin_weird()
    # the third head of the totem pole
    print hair_badhaircut()
    print eyes_crosseyes()
    print ears_round()
    print nose_bignostrils()
    print mouth_mustachecovered()
    print chin_square()
    
import random 
#imports the random library before calling the function

def random_hair():
    # returns one of four possible hairs choosing randomly with one choice = random.randint(1,4)
    choice = random.randint(1,4)
    if choice == 1:
        return hair_badhaircut()
    elif choice == 2:
        return hair_long()
    elif choice == 3:
        return hair_morning()
    else:
        return hair_reverse()
    
def random_eyes():
    # returns one of four possible eyes choosing randomly with one choice = random.randint(1,4)
    choice = random.randint(1,4)
    if choice == 1:
        return eyes_crosseyes()
    elif choice == 2:
        return eyes_leftlooking()
    elif choice == 3:
        return eyes_normal()
    else:
        return eyes_rightlooking()
    
def random_ears():
    # returns one of four possible ears choosing randomly with one choice = random.randint(1,4)
    choice= random.randint(1,4)
    if choice == 1:
        return ears_earrings()
    elif choice == 2:
        return ears_normal()
    elif choice == 3:
        return ears_round()
    else:
        return ears_twoholes()
    
def random_nose():
    # returns one of five possible noses choosing randomly with one choice = random.randint(1,5)
    choice= random.randint(1,5)
    if choice == 1:
        return nose_big()
    elif choice == 2:
        return nose_bignostrils()
    elif choice == 3:
        return nose_fourholes()
    elif choice == 4:
        return nose_small()
    else: 
        return ""
        

def random_mouth():
    # returns one of four possible mouths choosing randomly with one choice = random.randint(1,4)   
    choice = random.randint(1,4)
    if choice == 1:
        return mouth_full()
    elif choice == 2:
        return mouth_grumpy()
    elif choice == 3:
        return mouth_mustachecovered()
    else:
        return mouth_smiley()

def random_chin():
    # returns one of four possible chins choosing randomly with one choice = random.randint(1,4)
    choice = random.randint(1,4)
    if choice == 1:
        return chin_long()
    elif choice == 2:
        return chin_fat()
    elif choice == 3:
        return chin_square()
    else:
        return chin_weird()
    
def randompole():
    # randomly generates a head with part functions
    print random_hair()
    print random_eyes()
    print random_ears()
    nose = random_nose()
    if nose == "":
        pass
    else:
        print nose
    print random_mouth()
    print random_chin()

    
if __name__ == '__main__':
    # main function to print a totem pole
    # with three heads followed by random totem poles
    print "My totem pole"
    totem()
    print 
    print "My random totem pole"
    randompole()
    randompole()
    randompole()
    

