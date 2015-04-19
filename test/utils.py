import nltk

"""
    Converts the given text into a frequency list of the most common English words
    that aren't stop words.
"""
def extract(text):
    lower = text.lower()
    all_words = nltk.word_tokenize(lower)
    stopwords = nltk.corpus.stopwords.words("english")
    without_stopwords = [word for word in all_words if word not in stopwords]
    return without_stopwords