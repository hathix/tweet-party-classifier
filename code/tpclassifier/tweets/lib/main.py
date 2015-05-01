import utils
from tweet import Tweet
from party import Party
from classifier import Classifier

"""
    Creates and loads a Naive Bayes Classifier for the given list of Tweets to train on.
    Returns a Classifier object that you can run test(), accuracy(), etc. on.
"""
def get_classifier(tweets):
    # Size of the classifier's vocabulary. 
    # Increasing this value will increase accuracy at the cost of performance. 
    word_frequency_list_length = 1000

    words = utils.most_common_words([t.text for t in tweets], word_frequency_list_length)
    [t.load_freq_list(words) for t in tweets]
    classifier = Classifier(tweets, words)

    return classifier

"""
    Turns raw database tweet dicts into first-class Tweet objects.
"""
def parse_tweets(raw_tweets):
    return [Tweet(party=raw_tweet["party"], name=raw_tweet["name"], text=raw_tweet["raw_text"]) for raw_tweet in raw_tweets]