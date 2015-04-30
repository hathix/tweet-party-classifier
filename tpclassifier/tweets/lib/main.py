import utils
from tweet import Tweet
from party import Party
from classifier import Classifier

# testing
'''
corpus = [
    "This could be paradise",
    "Paradise? What's that?",
    "Dreams of paradise",
    "Welcome to Paradise",
    "I'm just a believer",
    "Believe in yourself"
]
sample = "Paradise but I give up"
sample2 = "I'm just a believer"

lis = most_common_words(corpus, 2)
print(freq_list(sample, lis))
print(freq_list(sample2, lis))
'''
'''
# todo keep the @'s around
tweets = [
    Tweet(Party.Democrat, "B. Obama", "Economy economy economy jobs jobs jobs healthcare"),
    Tweet(Party.Democrat, "H. Clinton", "..."),
    Tweet(Party.Republican, "M. Romney", "Jobs jobs jobs guns"),
    Tweet(Party.Republican, "J. McCain", "...")
]
cat = "Economy economy jobs healthcare guns"

words = utils.most_common_words([t.text for t in tweets], 2)
[t.load_freq_list(words) for t in tweets]

classifier = Classifier(tweets, words)
print(classifier.test(cat, Party.Republican))
print(classifier.test(cat, Party.Democrat))

if classifier.predict(cat) == Party.Republican:
    print "Republican"
else:
    print "Democrat"

testr = Tweet(Party.Democrat, "A. Traitor", "Jobs guns guns guns guns money")
print(classifier.accuracy([testr]))
'''

"""
    Creates and loads a Naive Bayes Classifier for the given list of Tweets to train on.
    Returns a Classifier object that you can run test(), accuracy(), etc. on.
"""
def get_classifier(tweets):
    # tweakable parameters
    word_frequency_list_length = 10

    words = utils.most_common_words([t.text for t in tweets], word_frequency_list_length)
    [t.load_freq_list(words) for t in tweets]
    classifier = Classifier(tweets, words)

    return classifier

"""
    Turns raw database tweet dicts into first-class Tweet objects.
"""
def parse_tweets(raw_tweets):
    return [Tweet(party=raw_tweet["party"], name=raw_tweet["name"], text=raw_tweet["raw_text"]) for raw_tweet in raw_tweets]