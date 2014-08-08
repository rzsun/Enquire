import tweepy
import json
import time
from sentclassifier import sentClassifier
from dashboard.models import Tweet
from pygeocoder import Geocoder

def getTweets(searchTerm):
	# TODO: check if classifier has been loaded
	classifier = sentClassifier(True, 'classifier.pickle')

	# Authentication details. To  obtain these visit dev.twitter.com
	consumer_key = '6F86k5I5SlRJhdCe2sPNIq5Lf'
	consumer_secret = 'fgRScFMqnXzEdsRPWWD26eq4AaN0RNNQQA6aE1NS1cWsJchu95'
	access_token = '989863279-pbCEbSGxlwpPdHj8LAHbjSnQg7FWCyqssosbI37f'
	access_token_secret = 'kWSENixo2ar4w21REKMhNW7zPiFCPUBY2e2gdWiiE3oAj'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	results = []
	for t in tweepy.Cursor(api.search,
		                       q=searchTerm,
		                       rpp=100,
		                       result_type="recent",
		                       include_entities=True,
		                       lang="en",
		                       geocode="39.5,-98.35,1500mi").items(5):
		myTweet = Tweet()
		myTweet.tweetText = t.text
		myTweet.sentiment = classifier(t.text)[0]
		myTweet.userName = t.user.screen_name
		myTweet.posProb = classifier(t.text)[1]
		myTweet.negProb = classifier(t.text)[2]
		myTweet.dateTime = t.created_at
		if(t.user.location is not None):
			locationCoords = Geocoder.geocode(t.user.location)
			myTweet.lat = locationCoords[0].coordinates[0]
			myTweet.lng = locationCoords[0].coordinates[1]
		myTweet.retweetCount = t.retweet_count
		myTweet.favoriteCount = t.favorite_count
		myTweet.followerCount = t.user.followers_count
		myTweet.save()
