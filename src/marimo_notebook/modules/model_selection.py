from typing import Optional, List, Dict
from lm_studio_integration import LMStudioClient

class ModelSelection:
    def __init__(self):
        self.lm_studio_client: Optional[LMStudioClient] = None
        self.available_models: List[Dict] = []

    def initialize_lm_studio(self):
        """Initialize LM Studio client and fetch available models"""
        self.lm_studio_client = LMStudioClient()
        try:
            lm_models = self.lm_studio_client.get_models()
            self.available_models.extend([
                {
                    "name": m["id"],
                    "type": "LM Studio",
                    "description": "Local model via LM Studio",
                    "config": {}
                }
                for m in lm_models.get("data", [])
            ])
        except Exception as e:
            print(f"Error initializing LM Studio: {e}")

    def get_available_models(self) -> List[Dict]:
        """Get list of all available models"""
        if not self.lm_studio_client:
            self.initialize_lm_studio()
        return self.available_models

    def select_model(self, model_name: str, model_type: str = "default"):
        """Select a model for use"""
        if model_type == "LM Studio":
            if not self.lm_studio_client:
                self.initialize_lm_studio()
            return {
                "client": self.lm_studio_client,
                "type": "LM Studio",
                "name": model_name
            }
        
        # Handle other model types
        return None

    def get_model_config_options(self, model_name: str, model_type: str) -> Dict:
        """Get configuration options for a specific model"""
        if model_type == "LM Studio":
            return {
                "temperature": {
                    "type": "float",
                    "default": 0.7,
                    "description": "Controls randomness in model responses"
                },
                "max_tokens": {
                    "type": "int",
                    "default": 1000,
                    "description": "Maximum number of tokens to generate"
                }
            }
        return {}