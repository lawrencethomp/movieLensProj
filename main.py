import csv
from pymongo import MongoClient, ReturnDocument
from process_reviews import median_reviews


# establish a connection to MongoDB.
client = MongoClient('mongodb://localhost:27017/')
db = client["movieLens"]

def get_genres(input_string):
    """
        processes the genre string and returns a Python list.
            input -- string of words separated by |
            returns -- a list of all genres.
    """
    genre_list = input_string.split("|")
    return genre_list

def add_movies():
    """
        open the csv of movies, and populate MongoDB.
            input - csv of the movies
            output - MongoDB instance
    """
    with open('./ml-20m/movies.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie = {
                "movieId":  row["movieId"],
                "title" : row["title"],
                "genre" : get_genres(row["genres"]),
                "rating": [],
            }
            db.movies.insert_one(movie)


# need to do it for ratings 2- 4001



def ratings_wrapper(chunk, first, last):
    """
        Exports reviews to the MongoDB.
            first - the first corresponding csv file.
            last - the last csv file.
            chunk - the csv fragment of the filesystem.

        NOTE: use progress to see what file was last, in case of file breakdown. 
     """
    for i in range(first, last):
        filename =  chunk +"%s.csv" % i
        add_reviews(filename)
        print("added files for: " + filename)
        with open("progress.txt", "a") as progress_file:
            progress_file.write('added reviews for: ' + filename + "\n")

def add_reviews(csv_ratings):
    """
        Adds the right reviews to the Mongo Document. 
        input csv_ratings - the filename to be converted to Dict.
    """
    with open(csv_ratings, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            db.movies.find_one_and_update(
                {"movieId": row["movieId"]},
                {"$push": {"rating": row["rating"]}},
                upsert=True,
                return_document=ReturnDocument.AFTER
            )

def aggregate_reviews():
    """
        Averages the score of reviews in an object and adds a key of median_values to the mongoDB item. 
    """
    # find all movies
    i = 0
    for document in db.movies.find(snapshot=True):
        # update with new category of median_reviews
        movie_reviews = document["rating"]
        movie_avg_score = median_reviews(movie_reviews)
        print(movie_avg_score)
        # push a new ranking from the document.
        document.update(
            {"average_rating": movie_avg_score},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        i = i + 1
        db.movies.save(document)
