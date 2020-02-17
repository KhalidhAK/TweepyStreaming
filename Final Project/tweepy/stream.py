from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# consumer key & secret
CONSUMER_KEY = "t2EGDozPRRXDoa2rYtQkXnWYw"
CONSUMER_SECRET = "L3EyOsXiM0I6SLePDWf9sjU1dNyVogjHgoDjx8Qmqdl6PCpPTO"

# access token
ACCESS_TOKEN = "3881605529-EmvIVAo28rkuMmmjPo70rJf2Y7aVXbg86Rh6Ts8"
ACCESS_TOKEN_SECRET = "GjcA5iXvPFnYsd0ElU5NhSFoLcryBYD37ELL8DsYdVm7E"



# listener that handles streaming data
class listener(StreamListener):
    print("Hello")
    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)
		
		
# OAuth process
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def main():
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["car"])