import os
import openai
from dotenv import load_dotenv

load_dotenv()



openai.api_key = os.getenv("OPENAI_API_KEY")
files = openai.File.list()

print(files.data)
