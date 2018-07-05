import tweepy
from textblob import TextBlob
import csv
from tweet_config import *

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

tweets = api.search("game of thrones", lang="en")

output = []
for tweet in tweets:
    output.append([tweet.text, TextBlob(tweet.text).sentiment])

with open('output.csv', 'w') as csvfile:
    tweet_write = csv.writer(csvfile, dialect='excel')
    tweet_write.writerows(output)