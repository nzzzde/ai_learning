import dotenv
import os
import anthropic

dotenv.load_dotenv()


client = anthropic.Anthropic()
model="claude-haiku-4-5-20251001"

message = client.messages.create(
  model=model,
  max_tokens=200,
  messages=[{
    "role": "user",
    "content": "How to become great AI Engineer? Give me a answer in 3 sentrences."
  }]
)
print(message.content[0].text)