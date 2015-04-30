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
        Predicts the party that was most likely to have authored the given text.
    """
    def predict(self, text):
        # optimization: because there are only 2 parties, we only need to check 1
        probability_democrat = self.test(text, Party.Democrat)
        if probability_democrat > 0.5:
            return Party.Democrat
        else:
            return Party.Republican
        '''
        probabilities = [(party, self.test(text, party)) for party in self.parties]
        sorted_pairs = sorted(probabilities, key=lambda pair: pair[1])
        most_likely_pair = sorted_pairs[-1]
        return most_likely_pair[0]
        '''

    """
        Returns a float representing the fraction of the time that the classifier
        correctly predicts the given testing tweets' parties.
    """
    def accuracy(self, tweet_list):
        correct = 0
        for tweet in tweet_list:
            if self.predict(tweet.text) == tweet.party:
                correct += 1
        return correct / len(tweet_list)

    """
        Runs the Naive Bayes classifier to determine the probability that the given text
        was authored by a member of the given party.
    """
    def test(self, text, party_guess):
        freq_list = utils.freq_list(text, self.word_list)
        # running the bayes predictor for each party
        probabilities = { party: self.bayes(party, freq_list) for party in self.parties }
        numerator = probabilities[party_guess]
        denominator = sum(probabilities.values())
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
    def bayes(self, party, sample_freq_list):
        party_tweets = self.tweets_by_party[party]
        prob_of_party = len(party_tweets) / len(self.tweets)
        feature_probs = []
        # iterate over every word (boolean flag)
        for i in xrange(0, len(sample_freq_list)):
            # P(A|B) = P(B|A) * P(A) / P(B)
            # P(match|party) = P(party|match) * P(match) / P(party)
            #                = P(match)
            # because we're only looking at the party's tweets
            num_matching = 0
            for test_tweet in party_tweets:
                if test_tweet.freq_list[i] == sample_freq_list[i]:
                    num_matching += 1
            probability = num_matching / len(party_tweets)
            feature_probs.append(probability)
        return prob_of_party * utils.product(feature_probs)

