import utils

"""
    Encapsulates a Tweet.

    Fields:
        party : Party   the sender's party
        name : string   the sender's name
        text : string   the tweet's text
"""
class Tweet:
    def __init__(self, party, name, text):
        self.party = party
        self.name = name
        self.text = text

    """
        Returns the frequency list (a list of 0's and 1's indicating if the Tweet contains
        top words from the word list) for the Tweet.
    """
    def get_freq_list(self, word_list):
        return freq_list(self.text, word_list)