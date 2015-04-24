from django.shortcuts import render

from .models import Tweet

def index(request):
	# list of tweets. each tweet is a dictionary with keys tweet_id, raw_text, name, party, etc.
	# ex. tweets[0]["raw_text"] gets the raw text of the first tweet
	# ex. tweets[0]["party"] gets 0 if author of first tweet is a Democrat, etc.
	tweets = Tweet.objects.all().values()

	#to use simple frontend, set accuracy to what you want displayed
	accuracy = 0

	num_tweets = Tweet.objects.count()

	# gets name: raw_text of random tweet
	random_tweet = Tweet.objects.order_by('?')[0]
	random_tweet_display = random_tweet.name + ": " + random_tweet.raw_text
	
	# sends accuracy, num_tweets, random_tweet_display to frontend
	context = {"accuracy": accuracy, "num_tweets": num_tweets, "random_tweet_display": random_tweet_display}
	return render(request, "tweets/index.html", context)
