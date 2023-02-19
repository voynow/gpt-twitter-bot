
import utils.twitter as twitter
import utils.gpt as gpt
import utils.trends as trends


def lambda_handler(event, context):

    trend = trends.get_trend()
    prompt = f"Create a dramatic tweet about tech and {trend}. Don't use the word tech. Use hashtags. Don't use emojis."
    model_engine = "text-davinci-003"

    tweet_resp = gpt.gen_tweet(model_engine, prompt)

    # don't tweet if invalid or test
    if 'msg' in tweet_resp or event['test']:
        return tweet_resp
    else:
        return twitter.tweet(tweet_resp['tweet'])._json



