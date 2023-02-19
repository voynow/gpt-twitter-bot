
import os

if not os.getcwd().endswith("tweet_lambda"):
    os.chdir("tweet_lambda")
import utils.twitter as twitter
import utils.gpt as gpt


# get all items from user timeline
timeline_items = []
timeline = twitter.get_user_timeline(cursorify=True)
for i, item in enumerate(timeline):
    timeline_items.append(item._json)

    if i > 300:
        raise ValueError("(Warning) Be mindful of Tweepy API limit of 900 requests/15 minutes")       

# range for deletion
id_range = {
    "max": 1626727032775139330,
    "min": 1624455861245468675
}

# iterate over timeline and delete tweets within id range
resps = []
for tweet in timeline_items:
    tweet_id = tweet['id']

    if tweet_id >= id_range['min'] and tweet_id <= id_range['max']:
        resp = twitter.delete(tweet_id)
        resps.append(resp)

# check for bad deletion resp
for resp in resps:
    if resp:
        print(resp)