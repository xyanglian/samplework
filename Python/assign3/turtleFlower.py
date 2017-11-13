'''
Created on Jan 26, 2015

'''
import turtle               # allows us to use the turtles library                                         
wn = turtle.Screen()        # creates a graphics window                                                    
                                                       
def flowerSquare(alex):
    # This function draws a flower by repeating squares
    for i in range(12):      # repeat twelve times
        # draw a square
        alex.forward(50)
        alex.left(90)
        alex.forward(50)
        alex.left(90)
        alex.forward(50)
        alex.left(90)
        alex.forward(50)
        alex.left(90) 
        # move 30 degrees 
        alex.left(30)
 
if __name__ == "__main__":       
    # main function to have a turtle draw a picture 
    alex = turtle.Turtle()    # create a turtle named alex
    flowerSquare(alex)


    wn.exitonclick()   # must be last line in file
