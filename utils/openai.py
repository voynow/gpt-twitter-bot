
import openai
from openai import Completion
import utils.secrets_manager as secrets_manager

openai.api_key = secrets_manager.get_secrets()['openai_secret_key']


def gpt_completion(
    model_engine,
    prompt,
    max_tokens=100,
    temperature=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.5,
    n=1,
    stop=None,
):

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        frequency_penalty=frequency_penalty, 
        presence_penalty=presence_penalty,
        n=n,
        stop=stop,
    )
    return completions.choices
