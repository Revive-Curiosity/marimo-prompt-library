from api_client import LMStudioClient
from config import LMStudioConfig

def initialize_lm_studio_model():
    config = LMStudioConfig()
    config.validate()
    return LMStudioClient()

def send_prompt_to_lm_studio(prompt: str, model: str = "default"):
    client = initialize_lm_studio_model()
    return client.send_prompt(prompt, model)

def list_lm_studio_models():
    client = initialize_lm_studio_model()
    return client.get_models()