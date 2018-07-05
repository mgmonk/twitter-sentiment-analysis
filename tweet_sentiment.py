import tweepy
from textblob import TextBlob
from tweet_config import *

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

tweets = api.search("Dodgers")

for tweet in tweets:
    print(tweet.text)
