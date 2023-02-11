
import twitter
import gpt
import utils

def lambda_handler(event, context):

    model_engine = "text-davinci-003"
    prompt = "Create an interesting tweet. Use as many hashtags as possible."

    body = gpt.gpt_completion(
        model_engine, 
        prompt, 
        frequency_penalty=2, 
        presence_penalty=2)
    resp = utils.clean_gtp_response(body)

    if 'msg' in resp:
        return resp
    else:
        return twitter.tweet(resp['tweet'])._json



