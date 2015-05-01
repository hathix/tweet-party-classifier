from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from utils import extract, freq_list
import tweet
from party import Party, ind_to_party
import numpy as np
from utils import most_common_words

class Classifier(object):
    """
        Loads the classifier with given training data and a list of words to watch for.
    """
    def __init__(self, training_tweets, vocabulary):
        self.clf = BernoulliNB()
        self.vocabulary = vocabulary
        self.train(training_tweets)
        
    def train(self, tweet_list):
        X_train, y_train = self.vectorize(tweet_list)
        self.clf.fit(X_train, y_train)

    def classify(self, text_or_tweet):
        """
            Guesses the party of the author of the given text (could be Tweet or other writing)
        """
        if type(text_or_tweet) is str or type(text_or_tweet) is unicode:
            x = freq_list(text_or_tweet, self.vocabulary)
        else:
            x = text_or_tweet.freq_list
        i = self.clf.predict(x)[0]
        return ind_to_party(i)

    def predict(self, t):
        """
            Alternate name for classify, introduced for compatibility
            with alternative implementation
        """
        return self.classify(t)

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
            features and a vector of Party labels, suitable for
            feeding as input to any scikit-learn classifier
        """
        y = [tweet.party for tweet in tweet_list]
        freq_lists = [tweet.freq_list for tweet in tweet_list]
        X = np.array(freq_lists)

        return X, y

    def test(self, text, party_guess):
        """
            Runs the Naive Bayes classifier to determine the probability that the given text
            was authored by a member of the given party.
        """
        x = freq_list(text, self.vocabulary)
        probas = self.clf.predict_proba(x)

        return probas[0][party_guess]