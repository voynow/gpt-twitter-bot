
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

    return tweepy.API(auth)


def tweet(message):
    """ 
    """
    api = get_auth()
    return api.update_status(message)


def get_timeline():
    """
    """
    api = get_auth()
    return api.home_timeline()


def get_user(user):
    """
    """
    api = get_auth()
    return api.get_user(user)


def delete_all_tweets():
    """
    """
    api = get_auth()
    for tweet in tweepy.Cursor(api.user_timeline).items():
        api.destroy_status(tweet.id)
