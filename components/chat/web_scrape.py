import requests
from bs4 import BeautifulSoup
from data.conversation import conversation
from data.global_variables import thinking
from functions.play_sound import play_sound
import openai
import random
import time


# Fetch request and convert html to text
def web_scrape(url, user_input, chat_window):
    thinking.set(True)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    proxies = []  # Example proxie array [{'http': 'http://proxy1'}, {'http': 'http://proxy2'}, ...]

    try:
        time.sleep(random.uniform(1, 5))
        proxy = random.choice(proxies) if proxies else None
        response = requests.get(url, headers=headers, proxies=proxy)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        image_links = [img['src'] for img in soup.find_all('img')]
        return gpt_webscrape_response(url, user_input, text, image_links, chat_window)
    except requests.exceptions.RequestException as e:
        conversation.append({"role": "assistant", "content": e})
        chat_window.update_conversation()
        play_sound('error')
        return thinking.set(False)

   
#Send web text to chatgpt
def gpt_webscrape_response(url, user_input, text, image_links, chat_window):
    thinking.set(True)
    try:
        prompt = f"{user_input}. This is the url {url} and this is the content -> '{text}'\n\nImage Links: {', '.join(image_links)}"
        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=0
        )
        response = completion.choices[0]['text']
        conversation.append({"role": "assistant", "content": response})
        play_sound("response")
    except openai.error.InvalidRequestError as e:
        error_message = "Error: " + str(e)
        conversation.append({"role": "assistant", "content": error_message})
        play_sound("error")
    except openai.error.AuthenticationError as e:
        error_message = "Error: " + str(e)
        conversation.append({"role": "assistant", "content": error_message})
        play_sound("error")
    finally:
        chat_window.update_conversation()
        thinking.set(False)

