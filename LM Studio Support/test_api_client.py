import pytest
import requests
from unittest.mock import Mock, patch
from api_client import LMStudioClient

def test_send_prompt():
    with patch("requests.post") as mock_post:
        mock_response = Mock()
        mock_response.json.return_value = {"choices": [{"text": "Test response"}]}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = LMStudioClient()
        response = client.send_prompt("Test prompt")

        assert response == {"choices": [{"text": "Test response"}]}
        mock_post.assert_called_once()

def test_get_models():
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {"data": [{"id": "model1"}]}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        client = LMStudioClient()
        response = client.get_models()

        assert response == {"data": [{"id": "model1"}]}
        mock_get.assert_called_once()

def test_send_prompt_error():
    with patch("requests.post") as mock_post:
        mock_post.side_effect = requests.exceptions.HTTPError("Test error")

        client = LMStudioClient()
        with pytest.raises(requests.exceptions.HTTPError):
            client.send_prompt("Test prompt")

def test_get_models_error():
    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.HTTPError("Test error")

        client = LMStudioClient()
        with pytest.raises(requests.exceptions.HTTPError):
            client.get_models()