import os
import pytest
from config import LMStudioConfig

def test_default_config():
    config = LMStudioConfig()
    assert config.server_url == "http://localhost"
    assert config.server_port == "1234"
    assert config.get_server_address() == "http://localhost:1234"

def test_custom_config(monkeypatch):
    monkeypatch.setenv("LM_STUDIO_SERVER_URL", "http://127.0.0.1")
    monkeypatch.setenv("LM_STUDIO_SERVER_PORT", "8080")
    config = LMStudioConfig()
    assert config.server_url == "http://127.0.0.1"
    assert config.server_port == "8080"
    assert config.get_server_address() == "http://127.0.0.1:8080"

def test_validation():
    config = LMStudioConfig()
    config.validate()  # Should not raise any errors

    config.server_url = ""
    with pytest.raises(ValueError, match="LM_STUDIO_SERVER_URL environment variable is required"):
        config.validate()

    config.server_url = "http://localhost"
    config.server_port = ""
    with pytest.raises(ValueError, match="LM_STUDIO_SERVER_PORT environment variable is required"):
        config.validate()

    config.server_port = "invalid"
    with pytest.raises(ValueError, match="LM_STUDIO_SERVER_PORT must be a valid integer"):
        config.validate()