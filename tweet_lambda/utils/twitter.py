
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
    return TWEEPY_API.update_status(message)


def get_user_timeline(cursorify=False):
    """
    """
    if cursorify:
        return tweepy.Cursor(TWEEPY_API.user_timeline).items()
    return TWEEPY_API.user_timeline()


def get_user(user):
    """
    """
    return TWEEPY_API.get_user(user)


def delete(tweet_id):
    """
    """
    TWEEPY_API.destroy_status(tweet_id)


# initialization for API obj
TWEEPY_API = get_auth()
