'''
Created on Sep 21, 2015

@author: xiaoyuyanglian
'''
def asl(measurable):
    a = measurable.count(".")
    b = measurable.count ("?")
    c = measurable.count ("!")
    d = len(measurable.split())
    if a == 0 and b == 0 and c == 0:
        return 0.0
    else:
        return d/float(a+b+c) 
    