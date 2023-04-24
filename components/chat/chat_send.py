# chat_submit.py
from dotenv import load_dotenv
from programs.chatgpt import ChatGPT

load_dotenv()


def user_response(input_field, chat_window, master, conversation):
    prompt = input_field.get('1.0', 'end-1c')
    user_message = {"role": "user", "content": prompt}
    conversation.append(user_message)

    chat_window.configure(state='normal')
    chat_window.insert('end', "User: " + user_message['content'] + "\n", 'user')
    chat_window.configure(state='disabled')
    chat_window.see('end')
    input_field.delete('1.0', 'end')
    master.after(100, assistant_response, chat_window, conversation)


def assistant_response(chat_window, conversation):    

    completion = ChatGPT(conversation)

    chat_window.configure(state='normal')
    chat_window.insert('end', "Assistant: " + completion + "\n", 'assistant')
    chat_window.configure(state='disabled')
    chat_window.see('end')
