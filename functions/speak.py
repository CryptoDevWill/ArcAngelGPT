import os
import tempfile
from gtts import gTTS
from playsound import playsound

def speak(text):
    tts = gTTS(text=text, lang='en')
    
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        temp_file = f"{fp.name}.mp3"
        tts.save(temp_file)
        playsound(temp_file)
        os.remove(temp_file)
