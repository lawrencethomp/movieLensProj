# movieLensProj
A COMP840 project about linear regression, and who likes what movies. A Lawrence and Oreva project for COMP840.


**Linear Regression:** A Linear Equation between two points of data. 

**What We Did:** Everyone likes movies, and we decided to ask the question: what determines whether or not someone would like a movie?

## The Properties: 
***
   The Properties currently in use are as follows:
   -  **movieId** ( _string_ ): The Id of the movie, used to link the movie to MovieLens and IMDB. 
   -  **title** ( *string* ): The name of the movie, used to obtain the year of release and a human-friendly title.
   -  **genre** (*List*): The list of genres the movie is identified with.    
   -  **rating** (*List*): A list of floating numbers users have rated this movie.
   -  **average_rating** (*float*): A median review score averaged from ratings from all the users.
   -  **imdbId** (*string*): the ImdbId used to get information from IMDB via datasets or scraping.
   -  **imdbId** (*float*): a median review compiled of all reviews given by imdb users.
   -  **rom_com** (*Boolean*): if movie is a Romantic Comedy/Drama. MovieLens skews male, so these movies may rate low.
   -  **classic_movie** (*Boolean*): checks whether or not the movie was released before 1980.
   -  **release_year** (*Int*): the year the movie was released.
   -  **num_genres** (*Int*): the number of genres the movie has been identified as.
   -  **num_ratings** *(Int*): The number of reviews that have been submitted.
   -  **imdb_consensus** (*Boolean*): Used to see if imdb users rated this movie over 2.95

## The Architecture:
***
   -  **Jupyter Notebook/Lab:** used to intuitively interact with the Python code and manipulate Data.
   -  **Visual Studio Code:** used to write Python code and work with PyMongo.
   -  **PyMongo:** wraps the MongoDB database in Python code for easy use such as CRUD functionality.
   -  **MongoDB:** intakes the csv files to do data manipulation.

https://www.youtube.com/watch?v=CtKeHnfK5uA - 1st video
Explanatory Variable:  The x var

Dependent Variable: A variable we want to explain. The Y var. 

Whats the relationship between the two variables?

https://www.youtube.com/watch?v=uwwWVAgJBcM - Linear Regression Machine Learning (tutorial)

We need to use Gradient Descent.

Draw a line

Compute an error

Error value is going to say how are you going to redo this value.

Line is going to be the optimal line.

set the learning rate

Train our model


Slope is gonna be y = mx + b


**HYPOTHESIS:** 
You can find a correlation between certain movie scores from users and their genres -- 

**PREDICTION:** Comedy is going to score lower than other aggregates.
Calling that Film-Noir scores very high.
Horror scores low
Romantic comedy scores low

Split the file into 100000 line files
https://codehandbook.org/pymongo-tutorial-crud-operation-mongodb/

https://docs.python.org/2/library/csv.html
for row in csvread etc.

https://api.mongodb.com/python/current/installation.html

1.) Process scores by pushing values into a JSON.
  write persistant data.
  name - movie name
  id - MovieLens ID
  Genre - genre of the movieID
  Rating - an aggregate score of all the reviews

1.) Add the MongoDB index of the movies.
https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_one

Use updateOne after an index https://docs.mongodb.com/manual/reference/method/db.collection.updateOne/#db.collection.updateOne
https://api.mongodb.com/python/current/api/pymongo/collection.html?highlight=update#pymongo.collection.Collection.update_one


When the files are done uploading, throw some reduce on there 
http://book.pythontips.com/en/latest/map_filter.html
Probably going to have to do some MOnary
https://bitbucket.org/djcbeach/monary/wiki/Home
https://stackoverflow.com/questions/16249736/how-to-import-data-from-mongodb-to-pandas
http://alexgaudio.com/2012/07/07/monarymongopandas.html
