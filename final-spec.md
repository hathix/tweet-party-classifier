# Tweet-Party Classifier
Neel Mehta, Ajay Nathan, Saranya Vijayakumar, Samuel Lam.

## About
Uses the Naive Bayes Classifier to predict the political party of the author of a Tweet. Uses data from [Quorum Analytics](https://quorum.us).

## Data Procurement
Quorum has over 1 million labeled Tweets in their database. We will use these Tweets to train our classifier. We will be writing a small API to easily interact with the Tweet data. That API is currently under construction. 

## Interface

### Enums
* Party
  * 0: Democratic
  * 1: Republican
 
We story party using an Enum instead of a string; it is a useful abstraction that guards against accidentally mistyping identifier names and makes type annotations more descriptive.

### Objects

* Tweet
  * party : Party
  * name : str
  * text : str
  * freqlist : bool list
  * __init__(party : Party, name : str, text : str)
    * Generates the frequency list by running extract(text)
* Classifier (implementation of Naive Bayes Classifier)
  * train(Tweet list) : None
  * classify(str) : Party
    * Guesses the party of the author of the given text (could be Tweet or other writing)
  * accuracy(Tweet list) : float
    * Runs classify on the text of every Tweet and returns the percent of correct party classifications.

We could simply have represented a Tweet as a tuple, but to allow for an initializer that auto-generates the frequency list out of the Tweet text (and to allow for better abstraction), we use a Tweet object. The Classifier object lets us encapsulate the state of the Bayes Classifier.

### Functions
* get_tweets() : Tweet list
  * Reads in raw Tweet data and constructs a Tweet object out of each. Data acquisition under construction by Ajay.
* partition_tweets(Tweet list) : (Tweet list, Tweet list)
  * Randomly splits the given Tweet list into a training and a testing list.
* extract(str) : bool list
  * Uses NLTK to remove English stopwords, 

### Process

## Technical Specifications
This project uses Python 2 and Django. Check the [Readme](https://github.com/hathix/tweet-party-classifier/blob/master/README.md) for instructions on running on your own machine.

We use the [Natural Language Toolkit](http://www.nltk.org/) to simplify processing the raw Tweet text.

## Naive Bayes
Samuel

## Timeline
Writeup due Friday, April 17
- Create front end - Django app
- Write extract function
- Figure out how to get tweets from Quorum (data procurement)
- Write classifier - train and test

Friday, April 24
- Finish writing Naive Bayes classifier
- Interface
- Helper functions (like accuracy calculation)
- Finish front end
- Reach goals

Due: May 1
