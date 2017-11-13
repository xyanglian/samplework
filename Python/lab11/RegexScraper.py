'''
Created on Nov 29, 2015

@author: Liane Yanglian & Linda Zhou
'''
import re,urllib2

def scrape(pattern,url):
    source = urllib2.urlopen(url)
    text = source.read()
    #print "read",len(text),"characters"
    for m in re.finditer(pattern,text):
        if m:
            print m.groups()
def dukemath():
    pattern = r'math/faculty/(.*?)\"\>(.+?)\<'
    baseurl = "http://fds.duke.edu/db/aas/math/faculty"
    scrape(pattern,baseurl)
    
def chronicle():
    pattern=r'mailto:(\w+[.\w]*)@(\w+[.\w+]*)'
    baseurl="http://www.dukechronicle.com/page/contact"
    scrape(pattern,baseurl) 
    
def pubpol():
    pattern = r'(\w+[.\w]*)@(\w+[.\w+]*)'
    baseurl = "https://sanford.duke.edu/people-and-research/faculty-directory-list?title=&field_profile_faculty_title_tid=All&field_profile_academic_area_tid=All&field_faculty_discipline_tid=All&field_center_name_tid=All&term_node_tid_depth=All&page=2"
    for page in range(1,16):
        url = baseurl[:-1]+str(page)
        print "scraping",page
        scrape(pattern,url)
        
def biology():
    pattern = r'mailto:(\w+[.\w]*)@(\w+[.\w+]*)'
    baseurl ="https://biology.duke.edu/people/all-faculty/a"
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        url = baseurl[:-1]+ch
        print "scraping",ch
        scrape(pattern,url)
        
if __name__ == '__main__':
    #pubpol()
    #dukemath()
    #biology()
    chronicle()