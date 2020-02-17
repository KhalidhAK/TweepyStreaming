import tweepy
import numpy as np
import pandas as pd


# consumer key & secret
CONSUMER_KEY = "t2EGDozPRRXDoa2rYtQkXnWYw"
CONSUMER_SECRET = "L3EyOsXiM0I6SLePDWf9sjU1dNyVogjHgoDjx8Qmqdl6PCpPTO"

# access token
ACCESS_TOKEN = "3881605529-EmvIVAo28rkuMmmjPo70rJf2Y7aVXbg86Rh6Ts8"
ACCESS_TOKEN_SECRET = "GjcA5iXvPFnYsd0ElU5NhSFoLcryBYD37ELL8DsYdVm7E"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#for tweet in api.search('food',count = 100):
#    print(tweet.text)

df = pd.DataFrame(columns = ['Tweets', 'User', 'User_statuses_count', 
                             'user_followers', 'User_location', 'User_verified',
                             'fav_count', 'rt_count', 'tweet_date'])
							 
def stream(data, file_name):

    i = 0

    for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='en').items():

        print(i, end='\r')

        df.loc[i, 'Tweets'] = tweet.text

        df.loc[i, 'User'] = tweet.user.name

        df.loc[i, 'User_statuses_count'] = tweet.user.statuses_count

        df.loc[i, 'user_followers'] = tweet.user.followers_count

        df.loc[i, 'User_location'] = tweet.user.location

        df.loc[i, 'User_verified'] = tweet.user.verified

        df.loc[i, 'fav_count'] = tweet.favorite_count

        df.loc[i, 'rt_count'] = tweet.retweet_count

        df.loc[i, 'tweet_date'] = tweet.created_at

        df.to_excel('{}.xlsx'.format(file_name))

        i+=1

        if i == 1000:

            break

        else:

            pass
							 
#stream(data = ['food'], file_name = 'my_tweets')
#df.head()