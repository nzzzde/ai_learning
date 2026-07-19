import dotenv
import os
import anthropic
from httpx import stream

dotenv.load_dotenv()


client = anthropic.Anthropic()
model="claude-haiku-4-5-20251001"

messages = []

def add_user_message(messages, text):
    user_message = {
        "role": "user",
        "content": text,
    }
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {
        "role": "assistant",
        "content": text,
    }
    messages.append(assistant_message)

# def chat(messages, system = None):
#     params = {
#         "model": model,
#         "max_tokens": 200,
#         "messages": messages,
#     }
#     if system:
#         params["system"] = system

#     message = client.messages.create(**params)
#     return message.content[0].text

add_user_message(messages, "Write a Python function that checks a string for duplicate characters.")

with client.messages.stream(
    model=model,
    max_tokens=200,
    messages=messages
) as stream:
    for text in stream.text_stream:
        print(text, end="")

