
from typing import List


#If you want to change the token limit, you can pass it as an argument to the get_tokenz 
#tokens = get_tokenz(input_text, token_limit=5000)

def get_tokenz(input_text: str,conversation, chat_window, thinking, play_sound, token_limit: int = 4096) -> int:
    # Split the input text into a list of words
    words = input_text.split()
    
    # Count the number of words
    word_count = len(words)
    
    if word_count > token_limit:
        print("over limit")
        conversation.append({"role": "assistant", "content": f"Too many tokens {word_count}"})
        chat_window.update_conversation()
        play_sound('error')
        thinking.set(False)
        return
    
    return word_count
