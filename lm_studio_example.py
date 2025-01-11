import marimo

from marimo_notebook.modules.model_selection import ModelSelection
from marimo_notebook.modules.llm_module import LLMModule

model_selection = ModelSelection()
available_models = model_selection.get_available_models()

model_name = marimo.ui.dropdown(
    options=[m["name"] for m in available_models],
    label="Select a model"
)

model_type = marimo.ui.dropdown(
    options=[m["type"] for m in available_models],
    label="Select a model type"
)

prompt = marimo.ui.text_area(label="Enter your prompt")

if model_name.value and model_type.value and prompt.value:
    selected_model = model_selection.select_model(model_name.value, model_type.value)
    if selected_model:
        llm_module = LLMModule(selected_model["client"])
        response = llm_module.send_prompt(prompt.value)
        marimo.output.text(response)
    else:
        marimo.output.text("Invalid model selection")