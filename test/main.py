import utils
from tweet import Tweet
from party import Party
from classifier import Classifier

# Here be testing

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

# todo keep the @'s around
tweets = [
    Tweet(Party.Democrat, "B. Obama", "Economy economy economy jobs jobs jobs healthcare"),
    Tweet(Party.Republican, "M. Romney", "Jobs jobs jobs guns")
]
cat = "Economy economy healthcare guns"

words = utils.most_common_words([t.text for t in tweets], 2)
print(words)
[t.load_freq_list(words) for t in tweets]
for t in tweets:
    print(t.freq_list)

classifier = Classifier(tweets)
print(classifier.test(tweets[0], Party.Republican))
print(classifier.test(tweets[0], Party.Democrat))