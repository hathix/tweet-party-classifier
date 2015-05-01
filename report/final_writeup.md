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
We would suggest that you use abstractions as much as possible because it makes testing and reasoning easier
Use Python, and Django to build the frontend and manage a database
##Results

We used a Python list, while scikit-learn used a more efficient C array called numpy array. Numpy arrays are more efficient for math manipulations such as the ones used here. 

Here are our results for the Twitter library: 

**Number of Tweets: 118789**

**Most common words: http, today, w, https, thank, great, work, year, honor, us, tax, bill, congress, day, help, student, week, famili, join, hous, it, time, congrat, live, good**

For each tweet, an output with the accuracy of the Bayes test tells us how well it matched the tweet to the party. 


##Original Draft and Specs (Annotated)


###Original Draft: 
We changed our entire project from predicting voting to predicting parties. 

###Final Spec: 
We used much of the information from the technical spec:

The classifier is based on the Naive Bayes algorithm: the probabilty of a tweet is determined first by applying Bayes Rule to express P(label/feature) in terms of P(label) and P(features|label):

```

|                       P(label) * P(features|label)
|  P(label|features) = ------------------------------
|                              P(features)

```

The 'naive' assumption is then made that all features are independent, given the label:

```
|                       P(label) * P(f1|label) * ... * P(fn|label)
|  P(label|features) = --------------------------------------------
|                                         P(features)

```

Rather than computing P(features) explicitly, the algorithm
calculates the denominator for each label and then normalizes them so that they
sum to one:

```

|                       P(label) * P(f1|label) * ... * P(fn|label)
|  P(label|features) = --------------------------------------------
|                        SUM[l]( P(l) * P(f1|l) * ... * P(fn|l) )

```

In order to find the most common words in the population of training data that are not stop words, this project utilizes our custom classifier with the class nltk.probability.FreqDist to identify top words.

```
from nltk.probability import FreqDist, DictionaryProbDist

```

- Collect_all_words method to return an array of all words from the training tweets
- The array is then passed to Identify_top_words method to identify the most frequent words
- nltk.FreqDist class : hash, sort the keys by their corresponding values, or counts
- We will obtain the top ### words with [:###]

```
def collect_all_words(self, items):
all_words = []
for item in items:
for w in item.all_words:
words.append(w)
return all_words

def identify_top_words(self, all_words):
    freq_dist = nltk.FreqDist(w.lower() for w in all_words)
    return freq_dist.keys()[:###]
```

- Get the features for each tweet
- Run array of all_words to reduce to a smaller set object to eliminate duplicate words
- Iterate through top_words and compare to this set for presence or absence, a hash of ### Booleans is returned

```
def features(self, top_words):
    word_set = set(self.all_words)
    features = {}
    for w in top_words:
    features["w_%s" % w] = (w in word_set)
    return features

```

- Collect the training set of tweets and their individual features and pass them to algorithm
- Once the classifier is trained, we will iterate through the set of tweets that remain to be classified. The classifier will guess the category for each item.

```
for item in tweets_to_classify:
features = item.features(top_words)
category = classifier.classify(features)
```

For accuracy evaluation we can use the custom `classifier.accuracy` function.

```
print(classifier.accuracy(test_set))
```

###Functionality Checkpoint:
We followed our timeline and didn't change much from what we expected. 

##Questions:
####How good was your original planning?
Our original planning matched up pretty well to how we ended up implementing our project. Once we finalized what we were doing (party prediction versus voting prediction) we followed our timeline very closely.
####How did your milestones go?
We followed our milestones pretty well, without any time pressure. 
####What was your experience with design, interfaces, languages, systems, testing, etc.?
We had to learn how to use the Naive Bayes classifier and how to get the tweets from Quorum. We also found efficiency and accuracy to be an important tradeoff. We also wanted to get the accuracy to be as close as possible to the accuracy of scikit-learn. 

####What choices did you make that worked out well or badly?
We had to make choices about the tradeoff between accuracy and run time. We can change the training data to increase the accuracy at the cost of time. 
####What would you like to do if there were more time?
We are running the classifiers with a vocabulary containing common words, but we could improve the algorithm by selecting those words that maximize dispersion upon Republican/Democrat classes, like factor analysis. 

We could also try other approaches such as SVM or RandomForests. 


####What was each group member's contribution to the project?
Ajay: front end and created API to get tweets
Sam: Scikit-learn
Saranya: writeup and accuracy
Neel: Naive Bayes classifier and run time/accuracy improval 


