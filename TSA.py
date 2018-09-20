import tweepy
from textblob import  TextBlob

consumer_key='60iVP8AQ5Ld923pWKoIGkThwm'
consumer_secret='Fe1tJkbKLNgbWQpaZajgHPMbfb0ikBTRtZfcVDZ6WlfmlpLAHx'

access_token='818688523540647937-NxCh5QpA0JQVhfGubBrI3DGoltCg09M'
access_token_secret='G2TRupVJxH89bw41E5pbBTk02XL2oAcT6kGoYdjuaZEmX'


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
Public_tweets=api.search('TMKOC')

for tweet in Public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)