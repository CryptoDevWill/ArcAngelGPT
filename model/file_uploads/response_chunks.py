import os
import openai
import traceback
from controller.data.conversation import Conversation
from controller.play_sound import play_sound

openai.api_key = os.getenv("OPENAI_API_KEY")


def response_chunks(chunks, chat_window):
    print('its moving main')
    conversation = Conversation()
    try:
        combined_response = ""
        total_chunks = len(chunks)
        for idx, chunk in enumerate(chunks, start=1):
            print('its moving for loop')
            conversation.append({"role": "assistant", "content": f"Processing chunk {idx} out of {total_chunks} please wait..."})
            chat_window.update_conversation()
            prompt = f"{chunk['prompt']} this is the data. Only output the data asked for in the provided prompt. Do not add any extra details or text that has not been asked for. '{chunk['chunk']}'"
            play_sound("system")
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=1500,
                temperature=0
            )
            extracted_info = response.choices[0].text.strip()
            combined_response += extracted_info + " "
            conversation.append({"role": "assistant", "content": extracted_info})
            play_sound("response")
            chat_window.update_conversation()

        return combined_response.strip()

    except Exception as e:
        error_message = f"An error occurred: {str(e)}\n{traceback.format_exc()}"
        conversation.append({"role": "assistant", "content": error_message})
        chat_window.update_conversation()
        play_sound("error")
        return error_message
