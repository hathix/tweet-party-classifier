from django.db import models


class Tweet(models.Model):
	tweet_id = models.IntegerField(blank=True, null=True, help_text="Arbitrarily assigned ID to easily identify tweets")

	PARTY = ( (0, "Democrat"), (1, "Republican"), )
	party = models.IntegerField(blank=True, null=True, choices=PARTY, help_text="Party of tweet's author")

	name = models.CharField(max_length=255, blank=True, null=True, help_text="The person's name, including whether they are a Represenative or Senator")

	raw_text = models.CharField(max_length=255, blank=True, null=True, help_text="The tweet's raw text")
