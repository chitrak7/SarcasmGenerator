from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
from . import forms
from . import models
from . import tweets
def query(request):
    path = os.path.join("templates", "land.html")
    return render(request, "query.html")

def queryResults(request):
    if request.method == 'GET':
        query = request.GET["query"]
        tweet_lst = tweets.get_tweets(query)
        result = models.Results(query=query, tweets=tweet_lst)
        return render(request, "queryResult.html", {'result':result})
    else :
        return render(request, "error.html")
        
