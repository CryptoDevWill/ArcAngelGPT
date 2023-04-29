import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

fileId = openai.File.create(
  file=open("training_data/training_data.jsonl", "rb"),
  purpose='fine-tune'
)

print(fileId)
