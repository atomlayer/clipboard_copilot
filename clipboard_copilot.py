import pyperclip
import time
import pyautogui
from openai import OpenAI
from dict_list_autosave.fdict import fdict

config = fdict('config.json')


def generate_code_snippet(open_ai_api_client, prompt):
    print("< " + prompt)

    prompt = f"""Please generate a code snippet based on the user's input. Don't explain the code. Don't give any comments.


Input: {prompt}


code_snippet: """

    generated_data = open_ai_api_client.chat.completions.create(messages=[
        {
            "role": "system",
            "content": ""
        },
        {
            "role": "user",
            "content": prompt
        }],
        model='command-r:latest',
        temperature=config["temperature"],
        max_tokens=config["max_tokens"]
    )

    generated_data = generated_data.choices[0].message.content

    print(" >" + generated_data)

    return generated_data


def main_loop():
    open_ai_api_client = OpenAI(base_url=config["open_ai_url"],
                                api_key=config["api_key"])

    old_text = ""
    modified_text = ""
    while True:

        text = pyperclip.paste()
        text = text.strip()
        comment = str(text)

        is_request = False

        if text == "":
            continue

        if text[0:2] in ["//", "/*"]:
            text = text[2:]
            is_request = True
        elif text[0] == "#":
            text = text[1:]
            is_request = True

        if is_request == True and text != old_text and text != modified_text:
            print(text)

            new_text = generate_code_snippet(open_ai_api_client, text)

            if new_text != "":
                modified_text = new_text
                pyperclip.copy(modified_text)
                pyautogui.hotkey('ctrl', 'v')

            old_text = comment

            time.sleep(1)


if __name__ == '__main__':
    main_loop()
