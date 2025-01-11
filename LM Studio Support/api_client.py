import requests
from config import LMStudioConfig

class LMStudioClient:
    def __init__(self):
        self.config = LMStudioConfig()
        self.config.validate()
        self.base_url = self.config.get_server_address()

    def send_prompt(self, prompt: str, model: str = "default"):
        url = f"{self.base_url}/v1/completions"
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "prompt": prompt,
            "model": model,
            "max_tokens": 1000,
            "temperature": 0.7,
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_models(self):
        url = f"{self.base_url}/v1/models"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()