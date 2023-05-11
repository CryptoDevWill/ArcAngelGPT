import os
import openai
from controller.data.conversation import Conversation
from controller.play_sound import play_sound
from controller.speak import speak
from controller.data.global_variables import loading
from controller.utils.load_settings import load_settings


def _init(chat_window):
    load_settings()
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=Conversation.instance().get()
    )
    response = completion.choices[0].message.content
    print(response)
    Conversation.instance().append({"role": "assistant", "content": response})
    chat_window.update_conversation()
    play_sound("response")
#     speak(response)
    loading.set(False)