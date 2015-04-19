import nltk
import re

"""
    Converts the given text into a frequency list of the most common English words
    that aren't stop words.
"""
def extract(text):
    lower = text.lower()
    all_words = nltk.word_tokenize(lower)
    # remove stopwords
    stopwords = nltk.corpus.stopwords.words("english")
    without_stopwords = [word for word in all_words if word not in stopwords]
    # filter out non-words
    word_re = re.compile("\w+");
    content_words = [word_re.match(word) for word in without_stopwords]
    content_words_collapsed = [x.group() for x in content_words if x != None]
    # normalize by stemming (e.g. turn "running" into "run")
    stemmer = nltk.stem.snowball.EnglishStemmer()
    normalized = [stemmer.stem(word) for word in content_words_collapsed]
    # TODO STILL BUGS HERE! e.g. "remember" => "rememb" (b/c nature of stemmer)
    # wait what if you just stemmed all the words in the top 1000 too? that'd ensure consistency
    return normalized

print(extract("Remember when I broke you down to tears. I gave you a tear. So I bet my life on you. This could be paradise. We'd be wondering if you could come."))