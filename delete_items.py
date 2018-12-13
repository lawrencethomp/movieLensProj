from pymongo import MongoClient, ReturnDocument
from process_reviews import median_reviews
import re
from itertools import permutations

client = MongoClient('mongodb://localhost:27017/')
db = client["movieLens"]

