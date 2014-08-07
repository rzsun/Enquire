import tweepy
import json
import time
from sentclassifier import sentClassifier

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
		                       lang="en").items(10):
		tweetDict = {}
		tweetDict["time"] = str(t.created_at)
		tweetDict["text"] = t.text
		tweetDict["sent"] = classifier(t.text)
		tweetDict["retweetcount"] = t.retweet_count
		results.append(tweetDict)
	return json.dumps(results)

