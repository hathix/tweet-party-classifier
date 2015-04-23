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

def bayes(party, party_tweets, all_tweets, sample_tweet):
    prob_of_party = len(party_tweets) / len(all_tweets)
    feature_probs = []
    # iterate over every word (boolean flag)
    for i in xrange(0, len(sample_tweet.freq_list)):
        # P(A|B) = P(B|A) * P(A) / P(B)
        # P(match|party) = P(party|match) * P(match) / P(party)
        #                = P(match)
        # because we're only looking at the party's tweets
        matching_fn = lambda test_tweet: test_tweet.freq_list[i] == sample_tweet.freq_list[i]
        matching_tweets = filter(matchin_fn, party_tweets)
        probability = len(matching_tweets) / len(party_tweets)
        feature_probs.append(probability)


