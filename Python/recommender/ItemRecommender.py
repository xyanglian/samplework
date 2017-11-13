'''
Created on Dec 3, 2015

@author: Liane Yanglian & Linda Zhou
'''
import RecommenderEngine, json
import SimpleFoodReader

if __name__ == "__main__":
    # main function that reads data in the Book format and makes recommendations based only on using item averages
    (jitems,jratings) = SimpleFoodReader.getData("foodratings_example.txt")
    print "items = ",jitems
    print "ratings = ", jratings
    
    items = json.loads(jitems)
    ratings = json.loads(jratings)
    
    avg = RecommenderEngine.averages(items,ratings)
    print avg[0:5]