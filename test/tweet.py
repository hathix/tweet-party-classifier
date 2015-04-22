import utils

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
        self.freq_list = freq_list(self.text, word_list)