from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))#'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')

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message.content)
