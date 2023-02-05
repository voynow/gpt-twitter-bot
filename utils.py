
import secrets_manager
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

