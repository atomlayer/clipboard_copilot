# Clipboard Copilot

This program uses OpenAI's API (local models can also be used, e.g. with ollama) and clipboard monitoring to create a code snippet based on user input.

## Usage:

1. Run the script
2. Copy your code comment or prompt to the clipboard (code comment must start with #, // or /*).
3. The generated snippet replaces the selected text, and you can use it immediately.


## Configuration:

The script's behavior is controlled by a JSON file named `config.json`. You can modify settings like `open_ai_url`, `api_key`, `temperature`, and `max_tokens` there.