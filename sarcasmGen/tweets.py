
import tweepy as tw
import os
import argparse

def get_tweets(topic, number=10):
    consumer_key = 'b6HJ5PwsBPuf1lIMmHuSuwfHl'
    consumer_secret = 'L6LNcDVcyilFWXjcNTL1hdlepysoVfH3WIHgSsnXEzWJNWC09h'
    access_token = '1221819988140363778-JY1ztl05wi6Vgz14x2CIcFK8My2RaC'
    access_token_secret = '3y2zq5HoOLkt1szgiqwdO2WadBMPSvBmr0xzBS0oL5taZ'

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tw.API(auth)

    if topic is not None: # display tweets from a particular topic
        search_words = topic
        tweets2display = number
        date_since = "2018-11-16"

        new_search = search_words + " -filter:retweets"
        new_search

        tweets = tw.Cursor(api.search,
                            tweet_mode="extended",
                            q=new_search,
                            lang="en",
                            since=date_since).items(tweets2display)
            

    else: # display all tweets from the account
        tweets = api.home_timeline()
    res = []
    for tweet in tweets:
        res.append(tweet.full_text)
    return res

