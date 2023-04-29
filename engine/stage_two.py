# assistant_response.py
import openai
import re
from data.conversation import conversation
from dotenv import load_dotenv
from functions.play_sound import play_sound
from data.global_variables import loading
from data.global_variables import working_directory
from engine.stage_three import stage_three
load_dotenv()



def stage_two(chat_window, response):
    loading.set(True)
    play_sound("work_mode")
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Given the message: '{response}', generate an array of steps needed to be taken to complete the task as if the AI model is carrying out the task itself.",
        max_tokens=1500,
        temperature=0,
        n=1
    )
    response = completion.choices[0].text.strip()
    print(response)
   

    conversation.append({"role": "system", "content": response})
    chat_window.update_conversation()
    loading.set(False)
    print("Stage Two Done!")

   