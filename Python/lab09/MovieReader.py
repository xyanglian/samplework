'''
Created on Nov 5, 2015

@author: Liane Yanglian and Linda Zhou 
'''
import csv

def readandprocess(name):
    csvf = open(name,'rb')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    datad = {}
    header = freader.next()
    decades={"40s":0,"50s":0,"60s":0,"70s":0,"80s":0,"90s":0,"00s":0,"10s":0}
    for row in freader:
        director = row[0]
        year=int(row[1])
        title=row[2]
        country=row[3]
        length=row[4]
        genre=row[5]
        color=row[6]
        if year>=1970 and year <=1979:
            decades["70s"]+=1
        if year>=1940 and year <=1949:
            decades["40s"]+=1
        if year>=1950 and year <=1959:
            decades["50s"]+=1
        if year>=1960 and year <=1969:
            decades["60s"]+=1
        if year>=1980 and year <=1989:
            decades["80s"]+=1
        if year>=1990 and year <=1999:
            decades["90s"]+=1
        if year>=2000 and year <=2009:
            decades["00s"]+=1
        if year>=2010 and year <=2019:
            decades["10s"]+=1
    return decades
print readandprocess("9600movies.csv")