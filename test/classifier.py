from party import Party
import tweet
import utils

class Classifier:

    def __init__(self, training_tweets):
        self.tweets = training_tweets
        self.parties = [Party.Republican, Party.Democrat]
        self.tweets_by_party = {}
        for party in self.parties:
            self.tweets_by_party[party] = filter(lambda tweet: tweet.party == party, self.tweets)

    def test(self, sample_tweet, party_guess):
        numerator = self.bayes(party_guess, self.tweets_by_party[party_guess], sample_tweet)
        denominator_list = [self.bayes(party, self.tweets_by_party[party], sample_tweet) for party in self.parties]
        denominator = sum(denominator_list)
        if denominator == 0:
            return 0
        else:
            return numerator / denominator

    # P(y = party) * product(P(x_i = u_i | y = party))
    def bayes(self, party, party_tweets, sample_tweet):
        prob_of_party = len(party_tweets) / len(self.tweets)
        feature_probs = []
        # iterate over every word (boolean flag)
        for i in xrange(0, len(sample_tweet.freq_list)):
            # P(A|B) = P(B|A) * P(A) / P(B)
            # P(match|party) = P(party|match) * P(match) / P(party)
            #                = P(match)
            # because we're only looking at the party's tweets
            matching_fn = lambda test_tweet: test_tweet.freq_list[i] == sample_tweet.freq_list[i]
            matching_tweets = filter(matching_fn, party_tweets)
            probability = len(matching_tweets) / len(party_tweets)
            feature_probs.append(probability)
        combined = prob_of_party * utils.product(feature_probs)
        return combined