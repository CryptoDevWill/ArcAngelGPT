import os
import openai
from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.File.delete("file-gcfUE8SwusYyr4t2M9aleJPR")
print(response)