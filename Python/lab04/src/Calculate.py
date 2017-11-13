'''
Created on Sep 14, 2015

@author: Liane Yanglian
'''


def process(name):
    f = open(name)
    answer = []
    for line in f:
        answer.append(line.strip())
    return answer          

def classAverage(grades):
    total = 0
    ppl = 0
    for i in grades:
        a = i.split(";")
        score = int(a[1])
        total = total + score
        ppl += 1
    return total/float(ppl) 

def howManyInRange(a,b,c):
    number = 0
    for i in a:
        a=i.split(";")
        if int(a[2]) >= b and int(a[2]) <= c: 
            number += 1 
    return number 
    
    
if __name__ == '__main__':
    filename = "grades.txt"
    data = process(filename)
    #for each in data:
        #print each
    #print
    print "Average grade is ", classAverage(data)
    year1 = 1991
    year2 = 1995
    print "Number born from ",year1,"to",year2,"is",
    print howManyInRange(data, year1, year2)


        
    