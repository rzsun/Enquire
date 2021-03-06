import tweepy
import json
import time
from sentclassifier import sentClassifier
from dashboard.models import Tweet
from pygeocoder import Geocoder

def getTweets(searchTerm):
	# TODO: check if classifier has been loaded
	classifier = sentClassifier(True, 'classifier.pickle')

	# Authentication details. To obtain these visit dev.twitter.com
	consumer_key = 'consumer_key'
	consumer_secret = 'consumer_secret'
	access_token = 'access_token'
	access_token_secret = 'access_token_secret'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	results = []
	
	#counter to bypass google geocode limit
	counter = 0;
	
	for t in tweepy.Cursor(api.search,
		                       q=searchTerm,
		                       rpp=100,
		                       result_type="recent",
		                       include_entities=True,
		                       lang="en",
		                       geocode="39.5,-98.35,1500mi").items(75):
		myTweet = Tweet()
		myTweet.tweetText = t.text.encode('utf-8')
		myTweet.sentiment = classifier(t.text)[0].encode('utf-8')
		myTweet.userName = t.user.screen_name.encode('utf-8')
		myTweet.posProb = classifier(t.text)[1]
		myTweet.negProb = classifier(t.text)[2]
		myTweet.dateTime = t.created_at
		if(t.user.location is not None):
			try:
				locationCoords = Geocoder.geocode(t.user.location)
				myTweet.lat = locationCoords[0].coordinates[0]
				myTweet.lng = locationCoords[0].coordinates[1]
			except:
				pass
			counter ++ 1
			if counter == 5:
				time.sleep(0.21)
				counter = 0
		myTweet.retweetCount = t.retweet_count
		myTweet.favoriteCount = t.favorite_count
		myTweet.followerCount = t.user.followers_count
		myTweet.chartKey = searchTerm.encode('utf-8')
		myTweet.save()
