import os
import openai
from data.conversation import conversation
from functions.play_sound import play_sound


def _init(chat_window):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
    )
    response = completion.choices[0].message.content
    conversation.append({"role": "assistant", "content": response})
    chat_window.update_conversation()
    play_sound("response")