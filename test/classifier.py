import party
import tweet
import utils

parties = [Party.Republican, Party.Democrat]
tweets_by_party = [[tweet for tweet in tweets if tweet.party == party] for party in parties]
# P(y = R) = len(tweets_by_party[Party.Republican]) / len(tweets)

def prob(party, tweet):
    # numerator
    party_tweets = tweets_by_party[party]
    prob_of_party = len(party_tweets) / len(tweets)
    feature_probs =
    numerator_probs = []
    for i in xrange(0, len(tweet.freq_list)):
        to_search = tweets_by_party[party]
        numerator_probs[i] = len([comp for comp in to_search if comp.freq_list[i] == tweet.freq_list[i]]) / len(to_search)
    # todo finish