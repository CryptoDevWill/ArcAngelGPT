from transformers import GPT2Tokenizer
from typing import List

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

#If you want to change the token limit, you can pass it as an argument to the get_tokenz 
#tokens = get_tokenz(input_text, token_limit=5000)

def get_tokenz(input_text: str,conversation, chat_window, thinking, play_sound, token_limit: int = 4096) -> int:
    tokens = tokenizer.encode(input_text)
    token_count = len(tokens)
    if token_count > token_limit:
        print("over limit")
        conversation.append({"role": "assistant", "content": f"Too many tokens {token_count}"})
        chat_window.update_conversation()
        play_sound('error')
        thinking.set(False)
        return
    
    return token_count
