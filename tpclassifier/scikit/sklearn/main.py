import utils
from utils import *
from tweet import Tweet, get_tweets_from_db as get_tweets
from party import Party, ind_to_party
from test_classifier import Classifier as TestClassifier
from sklearn_classifier import Classifier as SklearnClassifier
import time

def accuracytest(classifier_class, debug=False, nwords=2500):
    num_tweets, tweets = get_tweets()
    (train, test) = partition_tweets(tweets)
    corpus = [t.text for t in tweets]
    vocabulary = most_common_words(corpus, nwords)
    [t.load_freq_list(vocabulary) for t in tweets]
    classifier = classifier_class(train, vocabulary)
    
    return num_tweets, classifier.accuracy(train), classifier.accuracy(test)

def run_accuracy_reports():
    """Runs accuracy reports. Use to compare accuracy of both classifiers"""
    nwords = 1000
    num_tweets, accuracy_train, accuracy_test = accuracytest(SklearnClassifier, nwords=nwords)
    return nwords, num_tweets, accuracy_train, accuracy_test
