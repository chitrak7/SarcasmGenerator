from django.db import models

# Create your models here.

st = ["tttttttttttttttttttttttttttttttttttttt", "fdassasdfsafsafsafasdfasfasfas", "fsdfasfasfdsfasfasfsdfasfd", "fsdfasfsafasdfsdfsafsa"]

class Results :
    def __init__(self, query="sample", tweets=st, sentiment=0.5, sarcastic_response="yeah, right!"):
        self.query = query
        self.tweets = tweets
        self.sentiment = sentiment
        self.sarcastic_response = sarcastic_response
