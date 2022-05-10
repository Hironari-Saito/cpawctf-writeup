import os
import pandas as pd
import time
import tweepy


from datetime import timedelta
from dotenv import load_dotenv


load_dotenv(override=True)

# ConsumerKey
CK = os.getenv('TWITTER_CONSUMER_KEY')
# Consumer Secret
CS = os.getenv('TWITTER_CONSUMER_SECRET')
# Access Token
AT = os.getenv('TWITTER_ACCESS_TOKEN')
# Access Token Secret
AS = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# set authentication info
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

# create API instance
api = tweepy.API(auth,retry_count=5, retry_delay=2, timeout=500, wait_on_rate_limit=True)

# target
Account = 'porisuteru'
#Account = 'Kantei_Saigai'


tweets = tweepy.Cursor(api.user_timeline, screen_name=Account, exclude_replies=False,include_rts=False ).items()
time.sleep(.5)
count = 0
for tweet in tweets:
  print(tweet.created_at, tweet.user.name, ':', tweet.text)
  count += 1

print('SUM: %s' % count)
