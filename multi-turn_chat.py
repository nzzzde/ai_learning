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

def chat(messages, system = None):
    params = {
        "model": model,
        "max_tokens": 200,
        "messages": messages,
    }
    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text

add_user_message(messages, "Write a Python function that checks a string for duplicate characters.")
response = chat(messages,system="Respond as concisely as possible.")
add_assistant_message(messages, response)
print(response)

# while True:
#     user_input = input("Ask a question: ")
#     add_user_message(messages, user_input)
#     response = chat(messages)
#     add_assistant_message(messages, response)
#     print(response)

#     if input("Do you want to continue? (y/n): ").lower() != 'y':
#         print("Exiting the chat. Goodbye!")
#         break
