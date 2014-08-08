from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Tweet(models.Model):
    tweetText = models.CharField(max_length=145)
    userName = models.CharField(max_length=20)
    sentiment = models.CharField(max_length=5)
    posProb = models.FloatField(validators = [MinValueValidator(-1.0),
        MaxValueValidator(1.0)])
    negProb = models.FloatField(validators = [MinValueValidator(-1.0),
        MaxValueValidator(1.0)])
    dateTime = models.DateTimeField()
    lat = models.FloatField(validators = [MinValueValidator(-90.0),
        MaxValueValidator(90.0)])
    lng = models.FloatField(validators = [MinValueValidator(-180.0),
        MaxValueValidator(180.0)])
    retweetCount = models.IntegerField()
    favoriteCount = models.IntegerField()
    followerCount = models.IntegerField()
