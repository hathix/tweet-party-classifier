from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import TextForm

from .models import Tweet
import lib.main as main
import lib.utils as utils
from time import time

num_tweets = 1000

def index(request):
    # list of tweets. each tweet is a dictionary with keys tweet_id, raw_text, name, party, etc.
    # ex. tweets[0]["raw_text"] gets the raw text of the first tweet
    # ex. tweets[0]["party"] gets 0 if author of first tweet is a Democrat, etc.
    start = time()
    raw_tweets = Tweet.objects.all().values()
    first_tweets = raw_tweets[:num_tweets]
    print(time() - start)

    # to use simple frontend, set accuracy to what you want displayed
    tweets = main.parse_tweets(first_tweets)
    print(time() - start)
    training_tweets, testing_tweets = utils.partition(tweets)
    print(time() - start)
    classifier = main.get_classifier(training_tweets)
    print(time() - start)
    accuracy = classifier.accuracy(testing_tweets)
    print(time() - start)

    # gets name: raw_text of random tweet
    random_tweet = Tweet.objects.order_by('?')[0]
    random_tweet_display = random_tweet.name + ": " + random_tweet.raw_text

    most_common_words = utils.most_common_words([t.text for t in tweets], 25)
    most_common_str = ", ".join(most_common_words)
    
    # sends accuracy, num_tweets, random_tweet_display to frontend
    context = {"accuracy": accuracy, "num_tweets": num_tweets, "random_tweet_display": random_tweet_display, "most_common_words": most_common_str}
    return render(request, "tweets/index.html", context)

def predict(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        raw_tweets = Tweet.objects.all().values()
        first_tweets = raw_tweets[:num_tweets]

        # gets classifier
        tweets = main.parse_tweets(first_tweets)
        training_tweets, testing_tweets = utils.partition(tweets)
        classifier = main.get_classifier(training_tweets)
        
        raw_text = request.POST["raw_text"]

        return render(request, 'tweets/predict/predict.html', {'prediction': classifier.predict(raw_text)})

    return HttpResponse("<h1>Error</h1>")

    
