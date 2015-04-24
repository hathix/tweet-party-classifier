from __future__ import division
import nltk
import re
import operator
import random

# use normal english stopwords plus custom excluded twitter stopwords
english_stopwords = set(nltk.corpus.stopwords.words("english"))
twitter_stopwords = set(['http', 'https', 'rt', 'amp'])
stopwords = english_stopwords.union(twitter_stopwords)

word_re = re.compile("\w+")
stemmer = nltk.stem.snowball.EnglishStemmer()

"""
    Converts the given raw text into the basic (stemmed) forms of all the non-stopword
    English words contained therein.

    extract("I am running") = ["run"]
    extract("This could be paradise") = ["could", "paradis"]
"""
def extract(text):
    tokens = nltk.word_tokenize(text)
    words = [word.lower() for word in tokens]
    # remove stopwords
    without_stopwords = [word for word in words if word not in stopwords]
    # filter out non-words
    content_words = [word_re.match(word) for word in without_stopwords]
    content_words_collapsed = [x.group() for x in content_words if x != None]
    # normalize by stemming (e.g. turn "running" into "run")
    normalized = [stemmer.stem(word) for word in content_words_collapsed]
    return normalized

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
    product([1,2,3]) = 6
"""
def product(nums):
    return reduce(operator.mul, nums, 1)

"""
    Randomly splits a list of data items into a training set and a test set.
"""
def partition(data):
    train_ratio = 2 / 3

    shuffled = random.sample(data, len(data))
    # first (len * train_ratio) elements are training, rest are testing.
    split_index = int(len(shuffled) * train_ratio)
    training = shuffled[:split_index]
    testing = shuffled[split_index:]
    return (training, testing)