'''
Created on Nov 24, 2015

@author: Liane Yanglian & Linda Zhou
'''
import RecommenderEngine, json
import SimpleFoodReader

if __name__ == "__main__":
    # main function that calls functions in RecommenderEngine
    (jitems,jratings) = SimpleFoodReader.getData("foodratings_example.txt")
    print "items = ",jitems
    print "ratings = ", jratings
    
    items = json.loads(jitems)
    ratings = json.loads(jratings)
    
    avg = RecommenderEngine.averages(items,ratings)
    print avg
     
    for key in ratings:
         slist = RecommenderEngine.similarities(key,ratings)
         print key,slist
         print "\t",RecommenderEngine.scores(slist,items,ratings,1)
         print "\t",RecommenderEngine.scores(slist,items,ratings,len(slist))
