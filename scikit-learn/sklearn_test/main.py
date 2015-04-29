import utils
from utils import *
from tweet import Tweet, get_tweets_from_db as get_tweets
from party import Party, ind_to_party
from test_classifier import Classifier as TestClassifier
from sklearn_classifier import Classifier as SklearnClassifier
import time

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
Runs accuracy tests for specified classifier.
Parameters:
@classifier_class: the classifier to be tested.
@nwords: vocabulary size.
"""
def accuracytest(classifier_class, debug=False, nwords=2500):
    tweets = get_tweets()
    (train, test) = partition_tweets(tweets)
    corpus = [t.text for t in tweets]
    vocabulary = most_common_words(corpus, nwords)
    [t.load_freq_list(vocabulary) for t in tweets]
    classifier = classifier_class(train, vocabulary)
    
    print "Vocabulary size: %d" % nwords            
    print("Accuracy of classifier in train set: %.3f" % classifier.accuracy(train))
    print("Accuracy of classifier in test set: %.3f" % classifier.accuracy(test))

'''
Runs accuracy reports
Use to compare accuracy of both classifiers
'''
def run_accuracy_reports():
    print "\n"
    print "####### Running accuracy test... ####### "
    print "\n*********** sklearn_classifier ************"
    start = time.time()
    accuracytest(SklearnClassifier, nwords=2500)
    end = time.time()
    print "Total running time: %.2f secs" % (end - start)

if __name__ == '__main__':
    run_accuracy_reports()