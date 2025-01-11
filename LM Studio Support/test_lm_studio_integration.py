import pytest
from unittest.mock import Mock, patch
from lm_studio_integration import (
    initialize_lm_studio_model,
    send_prompt_to_lm_studio,
    list_lm_studio_models,
)

def test_initialize_lm_studio_model():
    with patch("lm_studio_integration.LMStudioClient") as mock_client:
        mock_client.return_value = Mock()
        client = initialize_lm_studio_model()
        assert client is not None

def test_send_prompt_to_lm_studio():
    with patch("lm_studio_integration.LMStudioClient") as mock_client:
        mock_client_instance = Mock()
        mock_client_instance.send_prompt.return_value = {"choices": [{"text": "Test response"}]}
        mock_client.return_value = mock_client_instance

        response = send_prompt_to_lm_studio("Test prompt")
        assert response == {"choices": [{"text": "Test response"}]}

def test_list_lm_studio_models():
    with patch("lm_studio_integration.LMStudioClient") as mock_client:
        mock_client_instance = Mock()
        mock_client_instance.get_models.return_value = {"data": [{"id": "model1"}]}
        mock_client.return_value = mock_client_instance

        response = list_lm_studio_models()
        assert response == {"data": [{"id": "model1"}]}

def test_send_prompt_to_lm_studio_error():
    with patch("lm_studio_integration.LMStudioClient") as mock_client:
        mock_client_instance = Mock()
        mock_client_instance.send_prompt.side_effect = Exception("Test error")
        mock_client.return_value = mock_client_instance

        with pytest.raises(Exception):
            send_prompt_to_lm_studio("Test prompt")

def test_list_lm_studio_models_error():
    with patch("lm_studio_integration.LMStudioClient") as mock_client:
        mock_client_instance = Mock()
        mock_client_instance.get_models.side_effect = Exception("Test error")
        mock_client.return_value = mock_client_instance

        with pytest.raises(Exception):
            list_lm_studio_models()