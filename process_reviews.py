"""
    Filename - process_reviews.py
    Author - Lawrence Thompson
    Date - 11/20/2018
    Class - COMP840

    Process reviews takes a review array, and gives a median.
"""

# import statements
from functools import reduce



def median_reviews(reviews):
    """
    gives a median of all arrays by adding all reviews together in file,
    then divides them by the length of the review array.

    INPUTS:
        reviews: a list of all reviews, floating numbers.
    """
    
    reviews = [float(i) for i in reviews]
    if len(reviews) == 0:
        return 0
    total = reduce((lambda x, y: x + y), reviews)
    median_reviews = round((total/len(reviews)), 2)
    return median_reviews

# median_reviews(movie_reviews)