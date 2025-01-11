import pytest
import sys
import os
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'LM Studio Support')))
from marimo_notebook.modules.model_selection import ModelSelection

def test_initialize_lm_studio():
    with patch("marimo_notebook.modules.model_selection.LMStudioClient") as mock_client:
        mock_client_instance = Mock()
        mock_client_instance.get_models.return_value = {
            "data": [{"id": "model1"}, {"id": "model2"}]
        }
        mock_client.return_value = mock_client_instance

        model_selection = ModelSelection()
        model_selection.initialize_lm_studio()

        assert len(model_selection.available_models) == 2
        assert model_selection.available_models[0]["name"] == "model1"
        assert model_selection.available_models[0]["type"] == "LM Studio"

def test_get_available_models():
    with patch("marimo_notebook.modules.model_selection.LMStudioClient") as mock_client:
        mock_client_instance = Mock()
        mock_client_instance.get_models.return_value = {
            "data": [{"id": "model1"}]
        }
        mock_client.return_value = mock_client_instance

        model_selection = ModelSelection()
        models = model_selection.get_available_models()

        assert len(models) == 1
        assert models[0]["name"] == "model1"

def test_select_lm_studio_model():
    with patch("marimo_notebook.modules.model_selection.LMStudioClient") as mock_client:
        mock_client_instance = Mock()
        mock_client.return_value = mock_client_instance

        model_selection = ModelSelection()
        result = model_selection.select_model("model1", "LM Studio")

        assert result["type"] == "LM Studio"
        assert result["name"] == "model1"
        assert result["client"] == mock_client_instance

def test_get_model_config_options():
    model_selection = ModelSelection()
    config = model_selection.get_model_config_options("model1", "LM Studio")
    
    assert "temperature" in config
    assert "max_tokens" in config
    assert config["temperature"]["type"] == "float"
    assert config["max_tokens"]["type"] == "int"