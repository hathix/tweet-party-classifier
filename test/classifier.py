from __future__ import division
from party import Party
import tweet
import utils

class Classifier:

    """
        Loads the classifier with given training data and a list of words to watch for.
    """
    def __init__(self, training_tweets, word_list):
        self.tweets = training_tweets
        self.word_list = word_list
        self.parties = [Party.Republican, Party.Democrat]
        self.tweets_by_party = {}
        for party in self.parties:
            self.tweets_by_party[party] = filter(lambda tweet: tweet.party == party, self.tweets)

    """
        Runs the Naive Bayes classifier to determine the probability that the given text
        was authored by a member of the given party.
    """
    def test(self, text, party_guess):
        freq_list = utils.freq_list(text, self.word_list)
        numerator = self.bayes(party_guess, self.tweets_by_party[party_guess], freq_list)
        denominator_list = [self.bayes(party, self.tweets_by_party[party], freq_list) for party in self.parties]
        denominator = sum(denominator_list)
        if denominator == 0:
            return None
        else:
            return numerator / denominator

    """
        Private helper function. Calculates
            P(y = party) * product(P(x_i = u_i | y = party))
        where u_i is the presence or absence of word i in the sample frequency list.

        Parameters:
            party : Party
            party_tweets : Tweet list       Tweets published by the given party.
            sample_freq_list : int list     The frequency list for a chunk of text.
        Returns: float
    """
    # P(y = party) * product(P(x_i = u_i | y = party))
    def bayes(self, party, party_tweets, sample_freq_list):
        prob_of_party = len(party_tweets) / len(self.tweets)
        feature_probs = []
        # iterate over every word (boolean flag)
        for i in xrange(0, len(sample_freq_list)):
            # P(A|B) = P(B|A) * P(A) / P(B)
            # P(match|party) = P(party|match) * P(match) / P(party)
            #                = P(match)
            # because we're only looking at the party's tweets
            matching_fn = lambda test_tweet: test_tweet.freq_list[i] == sample_freq_list[i]
            matching_tweets = filter(matching_fn, party_tweets)
            probability = len(matching_tweets) / len(party_tweets)
            feature_probs.append(probability)
        combined = prob_of_party * utils.product(feature_probs)
        return combined