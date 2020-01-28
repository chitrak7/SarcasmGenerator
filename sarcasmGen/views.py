from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
from . import forms
from . import models
from . import tweets
from . import sentiment
def query(request):
    path = os.path.join("templates", "land.html")
    return render(request, "query.html")

def queryResults(request):
    if request.method == 'GET':
        query = request.GET["query"]
        tweet_lst = tweets.get_tweets(query)
        senti = sentiment.get_sentiment(tweet_lst)
        result = models.Results(query=query, tweets=tweet_lst, sentiment=senti)
        return render(request, "queryResult.html", {'result':result})
    else :
        return render(request, "error.html")
        
