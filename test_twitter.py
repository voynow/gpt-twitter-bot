import twitter_utils as twitter_utils

api = twitter_utils.get_auth()

twitter_utils.tweet(api, "Sent this tweet using the Tweety Python package!")

twitter_utils.delete_all_tweets(api)