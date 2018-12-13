# movieLensProj
A Machine Learning project about linear regression, and who likes what movies. A Lawrence and Oreva project for COMP840.


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


## Getting the Data Together:
***
    1.)  Gathered the data from numerous sources - Kaggle, IMDB, and older MovieLens sets for demographics.
    2.)  Found a way to manipulate data - used MongoDB to process for the purposes of added data manipulation.
    3.)  Folded other CSVs into the MongoDB.
    4.)  Engineered Features and shrunk data.

## Hypothesis:
You can find a correlation between certain movie scores from users and their genres -- comedy is going to score lower than other aggregates; film-Noir scores very high, horror scores low, and romantic comedy scores low

## The Results: 
***
The most applicable source of data was the imdb_consensus boolean -- did the reviewers review the movie somewhere around the score of the movieLens item? On its own, Prestige and Awards do not have enough weight to determine a good movie -- many great movies will not win an award. However, we did find that it helped when they were added to the features, slightly. <br /> We were able to compile median scores on the data, and found more so that the number of genres related to the score of the item. So naturally, the genres became the number of genres data.
We didn't quite have anything that could solve the problem as the class item in Titanic would, but the data did a decent job working for us. Were there a more reliable way to source things like director, studio, and budget, this would have gone a little differently.
    
    
