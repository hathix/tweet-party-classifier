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
At first we wanted to use congressional data to predict how someone would vote in the future. We decided on comparing votes to parties to 
We also sped up our run time by removing the nltk word tokenizer, and just doing a custom split. 
####Unexpected problems
There was a tradeoff between accuracy and runtime. If we made the size of the vocab list larger, there would be better accuracy but it would take longer to run. Testing takes much longer than training because testing has to go through the entire tweet library.
####Advice for a future CS51 student


##Questions:
####How good was your original planning?
Good?
####How did your milestones go?
We followed our milestones pretty well, without any time pressure. 
####What was your experience with design, interfaces, languages, systems, testing, etc.?
We had to learn how to use the Naive Bayes classifier and how to get the tweets from Quorum. 
####What surprises, pleasant or otherwise, did you encounter on the way?
One surprise was how variable the run time and accuracy are. 
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

