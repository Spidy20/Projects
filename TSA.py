import tweepy
from textblob import  TextBlob

consumer_key='zSqsxVH82wRfIKYb7CFv6VchS'
consumer_secret='jKqmhKVmabBQX0ImTgHkDFi8iovAf0NCXYWBnarElEewuz5s4u'

access_token='818688523540647937-HYVdr7Co8972R6DRpwgzLK2suJk8AFf'
access_token_secret='nJWsi14Qp3WQsKN4zN39HNJfIjY3sn94seSZkD16MtoAX'


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
Public_tweets=api.search(' Donald trump ')

for tweet in Public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
