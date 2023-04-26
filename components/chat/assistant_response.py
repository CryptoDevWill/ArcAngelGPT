import openai
import os
from data.conversation import conversation
from dotenv import load_dotenv


load_dotenv()


def assistant_response():
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        response = completion.choices[0].message.content
        conversation.append({"role": "assistant", "content": response})
        print(conversation)