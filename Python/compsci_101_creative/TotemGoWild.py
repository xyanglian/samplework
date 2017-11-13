'''
Created on Sep 17, 2015

@author: Liane Yanglian
'''
    
import urllib2

def crawl(url):

    page = urllib2.urlopen(url)
    source = page.read()
    start = 0
    lurls = []
    while True:
        index = source.find("href=",start)
        if index == -1:
            break
        endq = source.find('"',index+6)
        nurl = source[index+6:endq]
        if nurl.startswith("totem"):
            lurls.append(nurl)
        start = endq+1
        
    #create a list with full URLs for each totem pole
    ret = []
    for tot in lurls:
        ret.append(url+"/"+tot)
    return ret

import random

def randomPole(urlList,size):
    for i in range(size):
        url=urlList[random.randint(1,len(data)+1)]
        source=urllib2.urlopen(url)
        st=source.read()
        print st

if __name__ == '__main__':
    mainUrl = "http://www.cs.duke.edu/courses/fall15/compsci101/assign/totem/uploads"
    data = crawl(mainUrl)
    print "number of URLs",len(data)
    randomPole(data, 6)




