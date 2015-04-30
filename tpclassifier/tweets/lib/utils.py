from __future__ import division
import nltk
import re
import operator
import random

# use normal english stopwords plus custom excluded twitter stopwords
english_stopwords = set(nltk.corpus.stopwords.words("english"))
twitter_stopwords = set(['http', 'https', 'rt', 'amp'])
stopwords = english_stopwords.union(twitter_stopwords)

word_re = re.compile("[A-Za-z_]+")
stemmer = nltk.stem.snowball.EnglishStemmer()

"""
    Converts the given raw text into the basic (stemmed) forms of all the non-stopword
    English words contained therein.

    extract("I am running") = ["run"]
    extract("This could be paradise") = ["could", "paradis"]
"""
def extract(text):
    tokens = nltk.word_tokenize(text)
    def clean_word(token):
        word = token.lower()
        return word
        # remove stopwords
        if word in stopwords:
            return None
        else:
            '''
            # filter out non-words
            word_match = word_re.match(word)
            if word_match == None:
                return None
            else:
            '''
            # normalize by stemming (e.g. turn "running" into "run")
            return stemmer.stem(word_match.group())
    cleaned_words = [clean_word(word) for word in tokens]
    # remove None's
    compacted_words = [x for x in cleaned_words if x != None]
    return compacted_words

"""
    Returns the n most common words in the given corpus of text.

    frequency_distribution(["a","b a","c c a"], 2) = ["a", "c"]
"""
def most_common_words(corpus, n):
    all_words = []
    for text in corpus:
        all_words.extend(extract(text))
    dist = nltk.FreqDist(all_words)
    # in format (word, frequency)
    most_common_tuples = dist.most_common(n)
    most_common = [pair[0] for pair in most_common_tuples]
    return most_common

"""
    For every word in word_list, sets the corresponding flag in the output
    to 1 if the word is in the given sample text and 0 otherwise.

    freq_list("a b c", ["a", "d"]) = [1, 0]
"""
def freq_list(sample, word_list):
    sample_words = set(extract(sample))
    word_set = set(word_list)
    flags = [1 if word in sample_words else 0 for word in word_set]
    return flags

"""
    Randomly splits a list of data items into a training set and a test set.
"""
def partition(data):
    train_ratio = 0.99

    shuffled = random.sample(data, len(data))
    # first (len * train_ratio) elements are training, rest are testing.
    split_index = int(len(shuffled) * train_ratio)
    training = shuffled[:split_index]
    testing = shuffled[split_index:]
    return (training, testing)