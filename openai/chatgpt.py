import os
import openai
from data.conversation import conversation
openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_completion():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return completion.choices[0].message

