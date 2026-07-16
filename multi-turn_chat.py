import dotenv
import os
import anthropic

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

def chat(messages):
    message = client.messages.create(
    model=model,
    max_tokens=200,
    messages=messages,
    )
    return message.content[0].text

add_user_message(messages, "How to become great AI Engineer? Give me a answer in 3 sentrences.")
response = chat(messages)
add_assistant_message(messages, response)
print(response)

add_user_message(messages, "Can you give me a more detailed answer in 5 sentences?")
response = chat(messages)
add_assistant_message(messages, response)
print(response)