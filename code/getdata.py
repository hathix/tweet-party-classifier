'''Run this code in Django shell to import tweets from file at PATH into db. Don't use otherwise'''

import csv

# from tweet models import Tweet

# data in this file must be in format: tweet_id, raw_text, party, name
PATH = "/Users/Ajay/Downloads/CS51project/tweets.csv"
NUM_TWEETS = 120

reader = csv.reader(open(PATH, 'rU'))

ctr = 0
temp = 2
for row in reader:
	# ensures that row is valid
	if len(row) == 5 and ctr < NUM_TWEETS:
		# maps party to enum
		if row[2] == "Democrat":
			temp = 0
		elif row[2] == "Republican":
			temp = 1
		else:
			temp = 2
		# creates and saves Tweet object for Democrats and Republicans only
		if temp != 2:
			tweet = Tweet(tweet_id = int(row[0]), raw_text = row[1], party = temp, name = row[3])
			tweet.save()

		ctr = ctr + 1

# for the sake of space, I only added the first NUM_TWEETS tweets to the testing db