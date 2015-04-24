from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from utils import extract, freq_list
from party import Party, ind_to_party
import tweet
import utils
import numpy as np

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

    def train(self, tweet_list):
        X_train, y_train = self.vectorize(tweet_list)
        self.clf.fit(X_train, y_train)

    def classify(self, text_or_tweet):
        """
            Guesses the party of the author of the given text (could be Tweet or other writing).
        """
        if type(text_or_tweet) is str or type(text_or_tweet) is unicode:
            x = freq_list(text_or_tweet, self.vocabulary)
        else:
            x = text_or_tweet.freq_list
        i = self.clf.predict(x)[0]
        return ind_to_party(i)

    """
        Predicts the party that was most likely to have authored the given text.
    """
    def predict(self, text):
        probabilities = [(party, self.test(text, party)) for party in self.parties]
        sorted_pairs = sorted(probabilities, key=lambda pair: pair[1])
        most_likely_pair = sorted_pairs[-1]
        return most_likely_pair[0]

    def accuracy(self, test_list):
        """
            Runs classify on the text of every Tweet and returns
            the percent of correct party classifications.
            Though it is possible to represent a Tweet as a tuple,
            in order to allow for an initializer that auto-generates the frequency list
            out of the Tweet text (and to allow for better abstraction), a Tweet object is used.
            The Classifier object encapsulates the state of the Bayes Classifier.
        """
        [t.load_freq_list(self.vocabulary) for t in test_list]
        X_test, y_test = self.vectorize(test_list)
        y_pred = self.clf.predict(X_test)
        return accuracy_score(y_test, y_pred)

    def vectorize(self, tweet_list):
        """
            Transforms a list of tweets into a matrix of boolean
            features and a vector of Party labels, this is suitable to
            feed as input to the scikit-learn classifier.
        """
        y = [tweet.party.value for tweet in tweet_list]
        freq_lists = [tweet.freq_list for tweet in tweet_list]
        X = np.array(freq_lists)
        return X,y

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