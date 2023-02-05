import utils.twitter as twitter
import utils.openai as openai

# api = twitter.get_auth()
# twitter.tweet(api, "Sent this tweet using the Tweety Python package!")
# twitter.delete_all_tweets(api)

# Generate text
model_engine = "text-davinci-002"
prompt = "Once upon a time, in a kingdom far far away,"

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=180,
    temperature=0.5,
    n=1,
    stop=None,
)

message = completions.choices[0].text
print(prompt + message)
