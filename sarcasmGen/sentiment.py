
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from . import tweets

def get_sentiment(tweets):
    ans = 0
    senti = SentimentIntensityAnalyzer()
    for tweet in tweets:
        score = senti.polarity_scores(tweet)
        ans += score["compound"]
        #print(str(score["compound"]) + "               " + tweet)
    return ans/len(tweets)
