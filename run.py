import tweepy
from textgenrnn import textgenrnn

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# 
textgenB = textgenrnn('twit.hdf5')

i=10

# tweet
import time
while i<100:    
    txt = textgenB.generate(1, return_as_list=True, temperature=1.0)[0]
    time.sleep(1)
    api.update_status(txt)
    print('tweeted successfully')
    i+=10
    time.sleep(5)
