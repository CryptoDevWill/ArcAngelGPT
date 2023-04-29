# assistant_response.py
import openai
from data.conversation import conversation
from dotenv import load_dotenv
from functions.play_sound import play_sound
from data.global_variables import thinking
from data.global_variables import username
from data.conversation import initial_system_prompt


load_dotenv()

print(initial_system_prompt)
def question(prompt, chat_window):
    thinking.set(True)
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Briefly answer {username}'s question - '{prompt}'. These are extra details incase you need them {initial_system_prompt}",
        max_tokens=500,
        temperature=0.3,
        n=1
    )

    response = completion.choices[0].text
    conversation.append({"role": "assistant", "content": response})
    chat_window.update_conversation()
    play_sound("response")
    thinking.set(False)
    