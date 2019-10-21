import tweepy
from textblob import textblob

consumer_key = 'c4hwVO0GeJNItenfQG0VOj9xh'
consumer_secret = 'LtzMbVQB9sKgPMrCgTuMuUpJsZaIhKBZ1vXBGaCri0M2qKWw27'

access_token = 	'115959819-vX0oFbHCbX2nO8O0qwE4BAy0gu46Z9Rwj6WbKWTH'
access_token_secret = 'n7HRvGs1UFsHnSzhsLpt5SMBvdkMgVeICjRWKKYSXC5hg'

auth = tweepy.OAuthHendler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search ('Bitcoin')

for tweet in public_tweets
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("")

if analysis <= 0
	print(ruim)

if analysis >= 0
	print(bom)

