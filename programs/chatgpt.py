# openai_chat.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Chat conversation
def ChatGPT(conversation):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        conversation.append({ "role": "assistant", "content": completion.choices[0].message.content })
        return completion.choices[0].message.content
    except openai.error.AuthenticationError as e:
        error_message = str(e)
        print(f"Error: {error_message}")
        return error_message
