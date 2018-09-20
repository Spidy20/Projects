import tweepy
from textblob import  TextBlob

consumer_key=' '
consumer_secret=''

access_token=''
access_token_secret=''


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
Public_tweets=api.search('TMKOC')

for tweet in Public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
