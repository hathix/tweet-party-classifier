###Progress:

* We set up Flask and Heroku, and picked the Naive Bayes classifier as our Machine learning algorithm. 

* We obtained the database of tweets from Quorum Analytics. We are using Django to manage our database. We also wrote the code to build a frequency list of words found in each tweet, as well as removes common words. extract (in utils.py) extracts the stemmed form of non-basic words.

* The class Tweet is defined with party, name, text, and freq_list. 

* We started working on the Bayes classifier and have a very basic front end set up.

###Problems:

* We had a problem finding the right algorithm, since we are using a list of booleans. Naive Bayes is not particularly built for a list of bools (and is normally used with something like heights or polling data. (see http://cs109.github.io/2014/pages/lectures/lecture14-bayesian-statistics.html#/)
* We are still having trouble pushing our large database to Git. Currently, we are using a smaller database to test our algorithm.
* We changed our project idea slightly after we met with Stefan. 

###Teamwork:

* We have split up the work pretty evenly. One problem we dealt with was working efficiently, which we dealt with by meeting together to get some work done. 

###Plan:
    
* We will be finishing the Bayes classifier and accuracy calculator. We will also set up a front end and set up the Tweet database. Neel will be doing the Bayes classifier, Sam will be working on the front end and routing, Ajay will be setting up the database, and Saranya will be writing the accuracy calculator. 
