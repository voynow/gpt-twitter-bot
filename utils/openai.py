
import openai
from openai import Completion
import utils.secrets_manager as secrets_manager

# Set the API key
openai.api_key = secrets_manager.get_secrets()['openai_secret_key']
