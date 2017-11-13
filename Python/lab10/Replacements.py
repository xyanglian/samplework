'''
Created on Nov 15, 2015

@author: Linda and Liane 
'''
import urllib2,random,os

repd = {}

def getReplacement(tag):
    '''
    returns a string/word to replace tag
    '''
    
    global repd
    
    # load the global dictionary if it hasn't been
    
    if len(repd.keys()) == 0:
        readfile()
        
    # shouldn't have <>, but check and be safe
    
    if tag.startswith("<"):
        end = tag.find(">")
        tag = tag[1:end]
    
    # check on tag, if not a key, try plural
    
    if not tag in repd:
        t = tag+'s'
        if not t in repd:
            return "NO-REPLACEMENT"
        else:
            tag = tag + 's'
            
    return random.choice(repd[tag])

def process(label,source):
    '''
    use source as a source of replacements
    for label, update global dictionary with
    choices for label, by adding to list for label
    '''
    
    global repd
    if source.startswith("http"):
        f = urllib2.urlopen(source)
    else:
        f = open(source)
        
    if label not in repd:
        repd[label] = []
    for line in f:
        repd[label].append(line.strip())
    
    f.close()
    #print label,repd[label]

def processfile(fname):
    head,tail = os.path.split(fname)
    dot = tail.find(".")
    label = tail[:dot]
    process(label,fname)

def readfile():
    basename = "tagreplacements"
    data = os.listdir(basename)
    for d in data:
        processfile(os.path.join(basename,d))
        
    #print repd

def readreps():
    url = "http://www.cs.duke.edu/csed/tag-a-story/tags";
    f = urllib2.urlopen(url)
    for line in f.readlines():
        pos = line.find("href=") 
        if pos != -1:
            start = pos+6
            end = line.find('"',start)
            sub = line[start:end]
            
            tagstart = line.find('>',end)
            tagend = line.find('<',tagstart)
            label = line[tagstart+1:tagend]
            process(label,url+"/"+sub)

if __name__ == '__main__':
    readreps()
    readfile()