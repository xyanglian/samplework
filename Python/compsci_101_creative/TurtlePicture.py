'''
Created on Sep 17, 2015

@author: Liane Yanglian
'''

import turtle # allows us to use the turtle
wn = turtle.Screen() #creates a graphics window
wn.bgcolor("pink") # sets the window background color

def picture():# creates a turtle and calls other functions
    glory = turtle.Turtle() # creates a turtle named glory
    glory.color("red") # sets the turtle's color to red
    glory.shape("turtle") # sets the turtle's shape as a turtle
    glory.speed(10) # makes the turtle go faster
    flowersquare(glory)
    direction(glory)
    trace(glory)
    backdirection(glory)
    circle(glory)
    flowersquare(glory)
    polygon(glory)
    stampy(glory)
    glow(glory)
    trace(glory)
    circle(glory)
    
def flowersquare(glory):
   # draws a flower square made out of squares
    colors = ["yellow","red","blue","purple","yellow","red","blue","purple","yellow","red","blue","purple","yellow","red","blue","purple","yellow","red","blue","purple"]
    for i in range (12): # repeats twelve times
        glory.color(colors[i])
        #draws a square
        glory.forward(50)
        glory.left(90)
        glory.forward(50)
        glory.left(90)
        glory.forward(50)
        glory.left(90)
        glory.forward(50)
        glory.left(90)
        # moves 30 degrees 
        glory.left(30)
        glory.forward(-10)
        
def direction(glory): #makes glory change direction and go forward
        glory.left(90)
        glory.forward(100)
        
def backdirection(glory): #makes glory change direction and go backwards
        glory.left(90)
        glory.forward(-70)

def trace(glory):# leaves a flower-like trace
    for i in range (8):
        for size in range(5,30,2):
            glory.stamp()
            glory.forward(size)
            glory.right(20)
            glory.down
    
def circle(glory): # makes a circle
    for i in range (4):
        glory.circle(120,360)    
        glory.dot (20,"blue")
        glory.forward(50)
        glory.circle(120.360)

def polygon(glory): # makes a polygon filled with color
    glory.begin_poly()
    glory.begin_fill() 
    glory.forward(100)
    glory.left(60)
    glory.forward(100)
    glory.left(60)
    glory.forward(100)
    glory.left(60)
    glory.forward(100)
    glory.left(60)
    glory.forward(100)
    glory.left(60)
    glory.forward(100)
    glory.end_fill()
    glory.end_poly()

def stampy(glory): # makes glory stamp many times in a row
    for i in range(8):
        glory.tilt(30)
        glory.stamp()
        glory.backward(20)
        glory.dot()
        
def glow(glory): # makes glory move and "glow" by changing its color 
    glory.right(90)
    glory.forward(300)
    glory.fillcolor("brown")
    glory.backward(10)

if __name__ == '__main__':
    #main function to have a turtle draw a picture 
    picture()

wn.exitonclick() # window stays up until clicked on 