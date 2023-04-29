# assistant_response.py
import openai
from data.conversation import conversation
from dotenv import load_dotenv
from functions.play_sound import play_sound
from data.global_variables import thinking


load_dotenv()


def peery(prompt, chat_window):
    thinking.set(True)
    completion = openai.ChatCompletion.create( 
        model="gpt-3.5-turbo", 
        messages=conversation
    )
    response = completion.choices[0].message.content
    conversation.append({"role": "assistant", "content": response})
    chat_window.update_conversation()
    play_sound("response")
    thinking.set(False)
    