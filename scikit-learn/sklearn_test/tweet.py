import utils
from utils import *
from party import Party
import pandas as pd
import sqlite3

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

'''
Fetchs tweets from testd.sqlite3 database and returns a list of Tweet classes.
'''
def get_tweets_from_db():
    con = sqlite3.connect('testdb.sqlite3')
    df = pd.read_sql('SELECT * from tweets_tweet', con)
    tweets= [Tweet(row['party'], row['name'], row['raw_text']) for i,row in df.iterrows()]
    return tweets