import utils
from utils import *
from party import Party

from tweets.models import Tweet as Tweets

"""
    Encapsulates a Tweet.

    Fields:
        party : Party   the sender's party
        name : string   the sender's name
        text : string   the tweet's text
        freq_list : int list  a list of 0's and 1's indicating if the Tweet contains certain words to watch for
"""
class Tweet:
    def __init__(self, party, name, text):
        self.party = party
        self.name = name
        self.text = text

    """
        Builds this Tweet's frequency list given a list of words to watch for.
    """
    def load_freq_list(self, word_list):
        self.freq_list = utils.freq_list(self.text, word_list)

"""
Fetches tweets from testd.sqlite3 database and returns a list of Tweet classes.
"""
def get_tweets_from_db():
    raw_tweets = Tweets.objects.all().values()
    
    # change this value to the same value as num_tweets in tweets.views to compare accuracy
    num_tweets = 1000
    first_tweets = raw_tweets[:num_tweets]
    
    tweets = [Tweet(party=raw_tweet["party"], name=raw_tweet["name"], text=raw_tweet["raw_text"]) for raw_tweet in first_tweets]
    return num_tweets, tweets