from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import tweetgetter
from sentclassifier import sentClassifier

def inputInfo(request):
	return render_to_response("sentclassify/inputinfo.html", {}, context_instance=RequestContext(request))
	
# TODO: change result to JSON
def result(request):
	if request.method == "POST":
		searchTerm = request.POST.get("searchterm", False)
		if(searchTerm != False):
			result = tweetgetter.getTweets(searchTerm)
			return render_to_response("sentclassify/result.html", {"result" : result}, context_instance=RequestContext(request))
		else:
			return render_to_response("sentclassify/inputinfo.html")

# TODO: custom filename parameter
def createClassifier(request):
	classifier = sentClassifier()
	classifier.saveClassifier("classifier.pickle")
	return HttpResponse("Classifier created at 'classifier.pickle'.")
