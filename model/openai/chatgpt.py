import os
import openai
from controller.data.conversation import Conversation
openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_completion():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=Conversation().get()
    )
    return completion.choices[0].message

