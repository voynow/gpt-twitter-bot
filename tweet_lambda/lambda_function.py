
import utils.twitter as twitter
import utils.gpt as gpt

def lambda_handler(event, context):

    model_engine = "text-davinci-003"
    prompt = "Create an interesting tweet about technology. Don't use the word technology. Use as many hashtags as possible."

    tweet_resp = gpt.gen_tweet(model_engine, prompt)

    # don't tweet if invalid or test
    if 'msg' in tweet_resp or event['test']:
        return tweet_resp
    else:
        return twitter.tweet(tweet_resp['tweet'])._json



