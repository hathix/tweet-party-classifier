import utils

"""
    Encapsulates a Tweet.

    Fields:
        party : Party   the sender's party
        name : string   the sender's name
        text : string   the tweet's text
        freqlist: bool list     enumerates the frequency of the most common English words in the tweet
"""
class Tweet:
    def __init__(self, party, name, text):
        self.party = party
        self.name = name
        self.text = text
        self.freqlist = utils.extract(self.text)