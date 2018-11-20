# movieLensProj
A COMP840 project about linear regression, and who likes what movies.


**Linear Regression:** A Linear Equation between two points of data. 

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
