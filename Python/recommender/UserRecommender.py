'''
Created on Dec 3, 2015

@author: Liane Yanglian & Linda Zhou
'''
import RecommenderEngine
import json
import random
import BookReader
import SimpleFoodReader
import MovieReader
import TestRecommender
import RecommenderEngine

if __name__ == "__main__":
    # main function that reads data in the Book format and creates UserRecommenderMovie.py to read data in the Movie format
    (jitems,jratings) = SimpleFoodReader.getData("foodratings_example.txt")
    print "items = ",jitems
    print "ratings = ", jratings
    
    items = json.loads(jitems)
    ratings = json.loads(jratings)
     
    randomperson1 = random.choice(ratings.keys())
    slist = RecommenderEngine.similarities(randomperson1, ratings)
    scores = RecommenderEngine.scores(slist, items, ratings, 5)
    print "Recommended scores:", scores[0:5]
    
    randomperson2 = random.choice(ratings.keys())
    slisttwo = RecommenderEngine.similarities(randomperson2, ratings)
    scores = RecommenderEngine.scores(slisttwo, items, ratings, 5)
    print "Recommended scores:", scores[0:5]