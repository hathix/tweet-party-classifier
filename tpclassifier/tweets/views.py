from django.shortcuts import render

from .models import Tweet

def index(request):
	# list of tweets. each tweet is a dictionary with keys tweet_id, raw_text, name, party, etc.
	# ex. tweets[0]["raw_text"] gets the raw text of the first tweet
	# ex. tweets[0]["party"] gets 0 if author of first tweet is a Democrat, etc.
	tweets = Tweet.objects.all().values()

	#to use simple frontend, set accuracy to what you want displayed
	accuracy = 0
	
	# sends accuracy to frontend
	context = {"accuracy": accuracy}
	return render(request, "tweets/index.html", context)
