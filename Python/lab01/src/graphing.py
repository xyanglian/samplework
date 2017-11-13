"""
Created on Jan 14, 2011

"""
# To do the lab, you will also need to use the math and random libraries.
import math         # used for question 3
import random       # used for question 4


def functionToGraph (x):
    """
    This is the function we will graph. It takes a single number, x, 
    and returns a single number, which is the value of this function 
    evaluated at that point. 
    """
    # TODO: Change this expression to experiment with the program
    return random.randint(0,20)


# You do not need to understand or modify this next function.
# We will go over it laster in the semester.
# We need to tell Python to use the plotting/graphing library.
import matplotlib.pyplot as plt
def displayFunctionGraph(start, end, numberOfPoints):
    """
    This function will graph the values of functionToGraph, described 
    above. This function produces and displays a graph of the function 
    evaluated over this range. It returns nothing.

    This function takes 3 numbers as arguments:
     - start is the value at which to start graphing
     - end is the value at which to finish graphing
     - numberOfPoints is the number of points at which to evaluate the function.
       They will be equally spaced out between start and end.
    """
    xValues = []  # Make empty lists to start
    yValues = []
    step = 1.0 * (end - start) / (numberOfPoints - 1)
    for i in range(numberOfPoints + 1):  # i = 0, 1, 2, ..., numberOfPoints
        x = start + i * step
        y = functionToGraph(x)
        xValues.append(x)
        yValues.append(y)
    plt.plot(xValues, yValues)
    plt.show()


# Now that we've defined our functions, call the main one.
# TODO: modify the numbers in parentheses to experiment with different plots
displayFunctionGraph(0, 20, 1000)
