import csv
from pymongo import MongoClient, ReturnDocument
import re

# an easy link to the file:
academy_file = './data_to_work/data_csv.csv'

client = MongoClient('mongodb://localhost:27017/')
db = client["movieLens"]

def get_genres():
    award_list = []
    with open('./data_to_work/data_csv.csv', encoding="utf8") as acawin:
        acawin = csv.DictReader(acawin)
        for row in acawin:
            if row["category"] not in award_list:
                award_list.append(row["category"])
                print(f'added {row["category"]} to awards')
                with open('check_awards.txt', "a") as awards_txt:
                    awards_txt.write(row["category"] + " \n ")

def format_movie_title(movie):
    # eliminate string info and 
    return movie.split("\(")[0]

def add_awards():
    with open('./data_to_work/data_csv.csv', encoding="utf8") as acawin:
        reader = csv.DictReader(acawin)
        i = 0
        for row in reader:
            outcome = 0
            if row["winner"] == "TRUE":
                outcome = 1
            db.movies.find_one_and_update(
                {"formatted_title" : row["entity"]},
                {"$push": {"awards": outcome}},
                upsert=True,
                return_document=ReturnDocument.AFTER
            )
            i = i + 1
            print(i)


# get_genres()

# add_awards()

def format_title(movie_name):
    regex = r'/\(.*\)/'
    formatted_title = re.sub(r'\(.*\)', '', movie_name)
    return formatted_title.rstrip()

def formatted_names():
    i = 0
    for document in db.movies.find(snapshot=True):
        new_title = (format_title(document["title"]))
        document.update(
            {"formatted_title": new_title}
        )
        db.movies.save(document)
        i = i + 1
        print(new_title + " " + str(i) )

# formatted_names()
add_awards()