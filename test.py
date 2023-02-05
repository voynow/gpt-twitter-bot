import utils

api = utils.get_auth()

utils.tweet(api, "Hey rachel! - from python")

utils.delete_all_tweets(api)