from pymongo import MongoClient, ReturnDocument
from process_reviews import median_reviews
import re

# establish a connection to MongoDB.
client = MongoClient('mongodb://localhost:27017/')
db = client["movieLens"]


# Python use JSON datatype https://realpython.com/python-json/

dict_list = []
# create a list of dictionarys

# iterate through to see if the value, a list of genres, is in the dictionary
genre_dict = {}
# genres the array
# the number of occurences

# input - a 

def parse_genres(genre_num):
    """

    """
    i = 0
    score = 0
    for document in db.movies.find({"num_genres": genre_num}):
        score = score + document["average_rating"]
        i = i + 1 
    avg = score/i
    print("Number of genres: " + str(genre_num) + " " + str(avg))

        # parses whether the genre is in the array

def check_genres():
    """
        displays the genres with their most frequent occurrences
    """
    