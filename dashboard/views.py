from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import tweetgetter
from sentclassifier import sentClassifier
import json
from dashboard.models import Tweet

def inputInfo(request):
	return render_to_response("dashboard/inputinfo.html", {}, context_instance=RequestContext(request))
	
# TODO: change result to JSON
def result(request):
	if request.method == "POST":
		searchTerm = request.POST.get("searchterm", False)
		numTweets = request.POST.get("searchterm", False)
		if(searchTerm is not False and numTweets is not False):
			tweetgetter.getTweets(searchTerm)
			return HttpResponse("Data successfully saved.")
		else:
			return HttpResponse("Error entered incorrectly.")
	

def dashboard(request):
	results = []
	for t in Tweet.objects.all():
		tweetDict = {}
		tweetDict["time"] = str(t.dateTime)
		tweetDict["text"] = t.tweetText.encode('utf-8')
		tweetDict["username"] = t.userName.encode('utf-8')
		tweetDict["sent"] = t.sentiment.encode('utf-8')
		tweetDict["posindex"] = t.posProb
		tweetDict["negindex"] = t.negProb
		tweetDict["lat"] = t.lat
		tweetDict["lng"] = t.lng
		tweetDict["retweetcount"] = t.retweetCount
		tweetDict["favoritecount"] = t.favoriteCount
		tweetDict["followercount"] = t.followerCount
		tweetDict["chartKey"] = t.chartKey
		results.append(tweetDict)
	return render_to_response("dashboard/dashboard.html", {"result" : json.dumps(results)}, context_instance=RequestContext(request))

# TODO: custom filename parameter
def createClassifier(request):
	classifier = sentClassifier()
	classifier.saveClassifier("classifier.pickle")
	return HttpResponse("Classifier created at 'classifier.pickle'.")
