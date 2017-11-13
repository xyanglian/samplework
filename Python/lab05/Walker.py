'''
Created on Sep 20, 2015

@author: Liane Yanglian
'''
import random
import turtle

tom = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)
tom.shape("square")
size = 20
def gcolor(val):
    x = 255 - 5*val
    if x < 0:
        x = 0
    return (x,x,x)



def walk(n,visualize,ycoord):

    current = 0
    visits = [0]*(2*n+1)
    
    if visualize:
        tom.penup()
        tom.color(255,255,255)
        tom.goto(0,ycoord)
        
    while visits.count(0) > 0:
        flip = random.randrange(0,2);
        if flip == 0:
            current += 1
        else:
            current -= 1
        if current > n:
            current = n
        if current < -n:
            current = -n
        visits[current+n] += 1
        if visualize:
            tom.stamp()
            vc = visits[current+n]
            tom.goto(size*current,ycoord)
            tom.color(gcolor(vc))
    #print current,visits
    return visits

if __name__ == "__main__":
    size = int(20)
    trials = int(41)
    total = 0
    ystart = 0
    for x in range(trials):
        results = walk(size,False,ystart)
        print sum(results),results
        total += sum(results)
        ystart += 25
    print "average for",trials,"walks of size",size,
    print total*1.0/trials
    
    wn.exitonclick()
