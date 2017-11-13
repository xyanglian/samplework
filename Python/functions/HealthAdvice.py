'''
Created on Sep 2, 2015

@author: ola
'''
import BMI

def getAdvice(name):
    print "hello",name,"how tall are you (in inches)?",
    inches = input(77)
    
    print "how much do you weigh (in pounds)",
    pounds = input(250)
    
    bmi = BMI.calculate(pounds,inches)
    
    if (bmi < 18.5):
        return "underweight"
    if (bmi < 24.9):
        return "healthy"
    if (bmi < 29.9):
        return "overweight"
    bmi = BMI.calculate(pounds, inches)
    return "obese"

x = getAdvice("owen")
print x