
import sys

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy.streaming import StreamListener

# consumer key & secret
CONSUMER_KEY = "t2EGDozPRRXDoa2rYtQkXnWYw"
CONSUMER_SECRET = "L3EyOsXiM0I6SLePDWf9sjU1dNyVogjHgoDjx8Qmqdl6PCpPTO"

# access token
ACCESS_TOKEN = "3881605529-EmvIVAo28rkuMmmjPo70rJf2Y7aVXbg86Rh6Ts8"
ACCESS_TOKEN_SECRET = "GjcA5iXvPFnYsd0ElU5NhSFoLcryBYD37ELL8DsYdVm7E"




auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = API(auth, wait_on_rate_limit=True,
          wait_on_rate_limit_notify=True)

class Listener(StreamListener):
    def __init__(self, output_file=sys.stdout):
        super(Listener,self).__init__()
        self.output_file = output_file
    def on_status(self, status):
        print(status.text, file=self.output_file)
    def on_error(self, status_code):
        print(status_code)
        return False

output = open('stream_output.txt', 'w')
listener = Listener(output_file=output)

stream = Stream(auth=api.auth, listener=listener)
try:
    print('Start streaming.')
    stream.sample(languages=['en'])
except KeyboardInterrupt:
    print("Stopped.")
finally:
    print('Done.')
    stream.disconnect()
    output.close()
