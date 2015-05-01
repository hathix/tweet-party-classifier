#Tweet Party Classifier

**Neel Mehta, Ajay Nathan, Saranya Vijayakumar, Sam Lam**

##Instructions

####Getting Started:

```git clone https://github.com/hathix/tweet-party-classifier.git```

```cd tweet-party-classifier```

```sudo pip install -r requirements.txt```

```python```

   - import nltk
  
   - nltk.download() # follow graphical installer
  
```python tpclassifier/manage.py runserver```

 open http://localhost:8000/tweets 

note: this project uses Python 2: (https://python.org)

####Scikit-learn

We hope to assess differences in accuracy between the scikit-learn implementation and our custom implementation. The classification and feature extraction pipeline has been tested with the
following library versions:

- Python 2.7.6

- nltk==3.0.2

- scikit-learn==0.15.1

- numpy==1.9.1

Running classifiers and/or comparing:

After installing requirements, in scikit-learn/sklearn_test, run

```python main.py```

This will

- fetch a list of sample tweets (fetched from included SQLite DB)
- create a vocabulary of frequent words
- turn the tweets into boolean vectors
- create training and test sets
- convert datasets to matrix form
- train a Bernoulli Naive Bayes classifier (best suited for boolean features)
- print out predicted results for a sample of the test data
- print out accuracy score over entire test data for classifier(s)


###Report on how things worked and what we learned

####How the project evolved
At first we wanted to use congressional data to predict how someone would vote on a given bill. We decided on comparing the language used by a congressman on Twitter to their party line: can the classifier correctly determine which party they are in based on their Tweets? This was more interesting to us because 

####Unexpected problems
There was a tradeoff between accuracy and runtime. If we made the size of the vocab list larger, there would be better accuracy but it would take longer to run. Testing takes much longer than training because testing has to go through the entire tweet library.
####Advice for a future CS51 student

##Results

![Sample Tweet]()

#####Number of Tweets: 118789
#####Most common words: http, today, w, https, thank, great, work, year, honor, us, tax, bill, congress, day, help, student, week, famili, join, hous, it, time, congrat, live, good


##Original Draft and Specs (Annotated)


###Original Draft: 


###Final Spec: 


###Functionality Checkpoint:


##Questions:
####How good was your original planning?
Our original planning matched up pretty well to how we ended up implementing our project. Once we finalized what we were doing (party prediction versus voting prediction) we followed our timeline very closely.
####How did your milestones go?
We followed our milestones pretty well, without any time pressure. 
####What was your experience with design, interfaces, languages, systems, testing, etc.?
We had to learn how to use the Naive Bayes classifier and how to get the tweets from Quorum. We also found efficiency and accuracy to be an important tradeoff. We also wanted to get the accuracy to be as close as possible to the accuracy of scikit-learn. 
####What surprises, pleasant or otherwise, did you encounter on the way?

####What choices did you make that worked out well or badly?

####What would you like to do if there were more time?
It might be interesting to use the information to determine how someone will vote in the future 
####How would you do things differently next time?

####What was each group member's contribution to the project?
Ajay: front end and created API to get tweets
Sam: Scikit-learn
Saranya: writeup and accuracy
Neel: Naive Bayes classifier and run time/accuracy improval 

####What is the most important thing you learned from the project?

