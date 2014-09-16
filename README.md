Enquire
=================
##Introduction
Enquire is a tool aiming to provide insight into the market’s overall sentiment on a product by analyzing Tweets. From the Tweets, companies can gain valuable information about how their products are perceived in the market and react accordingly.

It was created for Norton Engineering Hackathon 2014 where it won 2nd place.
##Implementation
Enquire works by streaming Tweets into a sentiment classifier which assigns to the Tweet a sentiment of either “positive” or “negative” as well as a numerical index. The impact of the Tweet can be found by using the sentiment index combined with the number of retweets and followers of that Tweet. The location of the Tweets are also geocoded and displayed onto a map to show the geodemographic Tweeters.
##Demo
http://twitterdashboard.herokuapp.com/home
##Usage
+ Enter OAuth credentials in dashboard/tweetgetter.py
+ Create a sentiment classifier by navigating to url/createclassifier
+ Navigate to url/input to enter search terms
+ Once you are done entering items, view the dashboard at url/dashboard!
