import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class LMStudioConfig:
    def __init__(self):
        self.server_url = os.getenv("LM_STUDIO_SERVER_URL", "http://localhost")
        self.server_port = os.getenv("LM_STUDIO_SERVER_PORT", "1234")

    def validate(self):
        if not self.server_url:
            raise ValueError("LM_STUDIO_SERVER_URL environment variable is required")
        if not self.server_port:
            raise ValueError("LM_STUDIO_SERVER_PORT environment variable is required")
        try:
            int(self.server_port)
        except ValueError:
            raise ValueError("LM_STUDIO_SERVER_PORT must be a valid integer")

    def get_server_address(self):
        return f"{self.server_url}:{self.server_port}"