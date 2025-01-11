# Marimo Prompt Library

A collection of prompts and tools for working with large language models.

## Features

-   **Prompt Library**: A collection of pre-built prompts for various tasks.
-   **Multi-LLM Prompting**: Tools for running prompts against multiple LLMs.
-   **Language Model Ranking**: Tools for ranking language models based on their performance.
-   **Ad-hoc Prompting**: Tools for quickly testing and iterating on prompts.
-   **LM Studio Support**: Integration with LM Studio for local model usage.

## Getting Started

1.  Clone the repository:

    ```bash
    git clone https://github.com/disler/marimo-prompt-library.git
    cd marimo-prompt-library
    ```

2.  Install the dependencies:

    ```bash
    pip install -e .
    ```

3.  Set up your environment variables. Create a `.env` file in the root directory and add the following:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ANTHROPIC_API_KEY=your_anthropic_api_key
    GOOGLE_API_KEY=your_google_api_key
    LM_STUDIO_SERVER_URL=http://localhost
    LM_STUDIO_SERVER_PORT=1234
    ```

    Replace the placeholder values with your actual API keys and LM Studio server details.

## LM Studio Integration

To use LM Studio with this library:

1.  **Install and Configure LM Studio**: Download and install LM Studio from [https://lmstudio.ai/](https://lmstudio.ai/). Start the LM Studio server.
2.  **Set Environment Variables**: Ensure that the `LM_STUDIO_SERVER_URL` and `LM_STUDIO_SERVER_PORT` environment variables are set correctly in your `.env` file.
3.  **Select LM Studio Model**: In the model selection UI, choose the LM Studio option and select your desired model.

## Usage

The library provides several modules for different tasks:

-   `prompt_library.py`: Contains functions for loading and managing prompts.
-   `multi_llm_prompting.py`: Contains functions for running prompts against multiple LLMs.
-   `language_model_rankings.py`: Contains functions for ranking language models.
-   `adhoc_prompting.py`: Contains functions for ad-hoc prompt testing.
-   `lm_studio_integration.py`: Contains functions for interacting with LM Studio.
-   `model_selection.py`: Contains functions for selecting and configuring models.

## Contributing

Contributions are welcome! Please submit a pull request with your changes.

## License

This project is licensed under the MIT License.