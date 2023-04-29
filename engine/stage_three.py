# assistant_response.py
import openai
from data.conversation import conversation
from dotenv import load_dotenv
from functions.play_sound import play_sound
from data.global_variables import loading

from data.global_variables import forbidden_commands

load_dotenv()



def stage_three(chat_window, response):
    loading.set(True)
    prompt ="",
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0
    )

    response = completion.choices[0].text.strip()
    print(response)
    conversation.append({"role": "system", "content": response})
    chat_window.update_conversation()
    loading.set(False)
    print("Stage Three Done!")