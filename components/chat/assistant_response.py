# assistant_response.py
import openai
import os
from data.conversation import conversation
from dotenv import load_dotenv
from data.global_variables import work_mode

load_dotenv()

def assistant_response(chat_window):
    if work_mode.get():
        work_response(chat_window)
    else:
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        response = completion.choices[0].message.content
        if '```' in response:
            work_mode.set(True)
            work_response(chat_window, response)
        else:
            print(response)
            conversation.append({"role": "assistant", "content": response})
            chat_window.update_conversation()

def work_response(chat_window, response):
    
    prompt = 'Only output an array string and nothing else of the steps needed to complete this task in order. Example: [{"instruction": "create folder named myfolder", "command": "mkdir myfolder"}, {"instruction": "create json file called jokes", "command": "touch jokes.json"}]. Here are the instructions ' + response

    chat_window.update_conversation()
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0
        )
    response = completion.choices[0].text
    print(response)
    conversation.append({"role": "assistant", "content": response})
    chat_window.update_conversation()
    work_mode.set(False)
