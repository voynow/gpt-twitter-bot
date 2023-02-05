
import utils.secrets_manager as secrets_manager
import tweepy

secrets = secrets_manager.get_secrets()


def get_auth():
    """
    """
    auth = tweepy.OAuthHandler(
        secrets['api_key'], 
        secrets['api_key_secret'])

    auth.set_access_token(
        secrets['access_token'], 
        secrets['access_token_secret'])

    return tweepy.API(
        auth=auth,
        wait_on_rate_limit=True)


def get_timeline(api):
    return api.home_timeline()


def tweet(api, message):
    api.update_status(message)


def get_user(api, user):
    api.get_user(user)


def delete_all_tweets(api):
    for tweet in tweepy.Cursor(api.user_timeline).items():
        api.destroy_status(tweet.id)
