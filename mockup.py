
from pymongo import MongoClient, ReturnDocument
from functools import reduce

# create an Array to simplify reviews using Reduce

movie_reviews = [4.0, 5, 3.5, 4, 3, 2.0, 2.2, 2.4, 2, 3, 1.5, 2.0, 2.5]

def median_reviews(reviews):
    total = reduce((lambda x, y: x + y), reviews)
    median_reviews = round((total/len(reviews)), 2)
    print(median_reviews)
    return median_reviews

median_reviews(movie_reviews)