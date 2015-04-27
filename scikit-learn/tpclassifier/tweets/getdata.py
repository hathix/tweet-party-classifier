import csv

PATH = "/Users/Ajay/Downloads/tweets.csv"

tweets = []

with open(PATH) as f:
	reader = csv.reader