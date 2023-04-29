import os
import openai
from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
finetune = openai.FineTune.create(model="davinci", training_file="file-gcfUE8SwusYyr4t2M9aleJPR")
print(finetune)