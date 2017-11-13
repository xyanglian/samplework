'''
Created on Nov 24, 2015

@author: xiaoyuyanglian
'''

from operator import itemgetter
def generate(results):
    d={}
    for item in results:
        itemsplit = item.split(" ")
        for num in range(len(itemsplit)):
            if num == 0:
                if itemsplit[num] in d:
                    d[itemsplit[num]][0] +=1
                else:
                    d[itemsplit[num]] = [1,0,0]

            if num == 1:
                if itemsplit[num] in d:
                    d[itemsplit[num]][1] +=1
                else:
                    d[itemsplit[num]] = [0,1,0]

            if num == 2:
                if itemsplit[num] in d:
                    d[itemsplit[num]][2] +=1
                else:
                    d[itemsplit[num]] = [0,0,1]
    org = [(k,v[0],v[1],v[2]) for (k,v) in d.iteritems()]
 
    organized = sorted(org, key=itemgetter(0))
    organizedd= sorted(organized, key=itemgetter(3),reverse=True)
    organizeddd= sorted(organizedd, key=itemgetter(2),reverse=True)
    final = sorted(organizeddd,key=itemgetter(1),reverse=True)
    finalstring = [(k,str(a),str(b),str(c)) for (k,a,b,c) in final]
    return [" ".join(x) for x in finalstring]