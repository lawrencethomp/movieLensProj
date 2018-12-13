"""
    Filename - main.py
    Author - Lawrence Thompson
    Date - 11/20/2018
    Class - COMP840

    Processes Excel Spreadsheet to give a median score.
"""

import csv
from pymongo import MongoClient, ReturnDocument
from process_reviews import median_reviews
import re
from itertools import permutations


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

def is_rom_com(genre_list):
    """
        parses to see if the movie is a romantic comedy.
        input - genre list
        output - boolean with True for romantic comedy, false for not
    """
    if len(genre_list) > 2: 
        return 0
    if "Romance" and "Comedy" in genre_list:
        return 1
    else:
        return 0

def is_classic_movie(movie):
    """
        checks all movies by title to see if movie is older than 1980.
        input - movie title with string in it.
        output - return True or False
        re for py \(\d{4}\)
    """
    
    title = re.findall(r'\(\d{4}\)', movie)
    year = int(title[0][1:5])	
    # return year
    if year < 1980:
        return 1
    else:
        return 0

def get_consensus():
    """
        Checks to see if movie is around a certain threshold of imdb score.
        2.75 will be what we define.
    """
    i = 0
    for document in db.movies.find({"imdbId_review": {"$exists": True}}):
        if document["imdbId_review"] > 2.95:
            document.update(
            {"imdb_consensus": 1},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        else:
            document.update(
            {"imdb_consensus": 0},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        print(i)
        i = i + 1
        db.movies.save(document)
get_consensus()

def compile_awards():
    for document in db.movies.find({"top_250": {"$exists": False}}):
        document.update({
            "top_250": 0
        })
        db.movies.save(document)

def do_score():
    for document in db.movies.find({"average_rating": {"$exists": True}}):
        if document["average_rating"] > 3.08:
            document.update({
                "over_under": 1
            })
        else:
            document.update({
                "over_under":0
            })
        print(document["over_under"])
        db.movies.save(document)

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

def add_imdb():
    with open('./ml-20m/links.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            db.movies.find_one_and_update(
                {"movieId": row["movieId"]},
                {"$set": {"imdbId": row["imdbId"]}},
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

def add_imdb_reviews():
    with open('./data.tsv', encoding="utf8") as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')
        i = 0
        for row in tsvin:
            print("Adding imdb review for: " + row[0][2:])
            db.movies.find_one_and_update(
                {"imdbId": row[0][2:] },
                {"$set": {"imdbId_review": float(row[1]/2)/2}},
                upsert=True,
                return_document=ReturnDocument.AFTER
            )
            i= i + 1
            print(i)

def average_reviews(snapshot=True):
    total = 0
    i = 0
    for document in db.movies.find({"average_rating": {"$exists": True}}):
        print(document['title'])
        print(document['average_rating'])
        print(i)
        total = total + document['average_rating']
        i = i + 1
    avg = total/i
    print(avg)

def correct_scores():
    i = 1
    for document in db.movies.find({ "$and" : [{"imdbId_review": {"$exists": True}}, {"movieId" : {"$exists": True}}]}):
        num = float(document["imdbId_review"])/2
        document.update(
            {"$set": {"imdbId_review": float(row[1]/2)/2}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        db.movies.save(document)
        print(str(num) + " " + str(i))        
        i = i + 1

def genre_scores():
    genre_array = [
                    "Action", "Adventure", "Animation", "Children", "Comedy", 
                    "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", 
                    "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]
    for i in range(2, 6):
        perm  = permutations(genre_array, i)
        for genres in list(perm):
            genres = list(genres)
            print(genres)
            genres_score = 0
            genres_index = 0
            not_genres_score = 0
            not_genres_index = 0
            for document in db.movies.find({ "$and" : [{"average_rating": {"$exists": True}}, {"movieId" : {"$exists": True}}]}):
                movie = document["title"]
                if document["genre"] == genres:
                    genres_score = genres_score + document["average_rating"]
                    genres_index = genres_index + 1
                    print(f"added {movie} to {genres}")

                if document["genre"] != genres:
                    not_genres_score = not_genres_score + document["average_rating"]
                    not_genres_index = not_genres_index + 1

                else:
                    not_genres_score = not_genres_score + document["average_rating"]
                    not_genres_index = not_genres_index + 1
            if genres_index > 3:    
                with open("genres.txt", "a") as genre_file:
                    genre_file.write(f"{genres} Score: " + str(genres_score/genres_index) + " \n")
                    genre_file.write(f" ALSO: {genres} had {genres_index} movies in this category" + " \n")
                    genre_file.write(f"Everything else that wasn't {genres} had {not_genres_index} movies" + " \n")
                    genre_file.write(f" \tEverything Else: " + str(not_genres_score/not_genres_index) + " \n \n")

def romcom():
    i = 1
    rom_com_score = 0
    rom_com_index = 0
    not_rom_com_score = 0
    not_rom_com_index = 0
    for document in db.movies.find({ "$and" : [{"imdbId_review": {"$exists": True}}, {"movieId" : {"$exists": True}}]}):
        if document["rom_com"] == 1:
            rom_com_score = rom_com_score + document["average_rating"]
            rom_com_index = rom_com_index + 1
            print(rom_com_score)
            print(rom_com_index)
        else:
            not_rom_com_score = not_rom_com_score + document["average_rating"]
            not_rom_com_index = not_rom_com_index + 1
            print(not_rom_com_score)
            print(rom_com_index)
    rom_com_med = rom_com_score/rom_com_index
    not_rom_com_med = not_rom_com_score/not_rom_com_index
    print("ROMCOM " + str(rom_com_med) )
    print("NOT ROMCOM " + str(not_rom_com_med))

def add_features():
    i = 1
    
    for document in db.movies.find({ "$and" : [{"imdbId_review": {"$exists": True}}, {"movieId" : {"$exists": True}}]}):
        print(document["title"])
        document.update(
            {"rom_com": is_rom_com(document["genre"])},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        # document.update(
        #     {"classic_movie": is_classic_movie(document["title"])},
        #     upsert=True,
        #     return_document=ReturnDocument.AFTER
        # )
        #             {"num_ratings": len(document["rating"])},
        # document.update(
        #     {"num_genres": int(len(document["genre"]))},
        #     upsert=True,
        #     return_document=ReturnDocument.AFTER
        # )
        db.movies.save(document)
        print(str(i))        
        i = i + 1

def add_imdb_top250():
    with open('./IMDB-Top-250.csv', encoding="utf8") as top250:
        reader = csv.DictReader(top250)
        for row in reader:
            db.movies.find_one_and_update(
                {"title": row["Title"]},
                {"$set" : {"top_250": 1}},
                upsert=True,
                return_document=ReturnDocument.AFTER
            )

def read_data():
    is_male = 0
    is_female = 0
    age = 0
    users = 0
    for line in open('./users.dat', 'r'):
        line = line.rstrip()
        line_list = line.split('::')
        user_age = line_list[2]
        user_gender = line_list[1] 
        if user_gender == 'M':
            is_male = is_male + 1
        else:
            is_female = is_female + 1
        age = age + int(user_age)
        print(line_list)
        users = users + 1
    gender_percentage_male = round(((is_male/users) * 100),2)
    gender_percentage_female = round(((is_female/users) * 100),2)
    print("male: " + str(is_male))
    print("female: " + str(is_female))
    print("median_age "+ str(age/users))
    print(users)
    print(is_female + is_male)
    print(gender_percentage_male)
    print(gender_percentage_female)
    with open("demographics.txt", "a") as demog_file:
        demog_file.write("Number of users: " + str(users) + " \n")
        demog_file.write("Percentage of men: " + str(gender_percentage_male) + " \n")
        demog_file.write("Percentage of women: " + str(gender_percentage_female) + " \n")
        demog_file.write("Age Demographic: " + str(age/users) + " \n")

